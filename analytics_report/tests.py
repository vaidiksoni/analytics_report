from django.test import TestCase
# Create your tests here.
import datetime
import pandas as pd
import logging
import pymysql.cursors
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def strip_lowercase(val):
    """" to remove extra spaces from the category name and to lowercase it."""
    return str(val).strip().lower()


def category_report(required_date):
    """return the category report as per the root categories"""
    try:
        cwsdt = required_date - datetime.timedelta(required_date.weekday())  # current week start date
        rwsdt = cwsdt - datetime.timedelta(weeks=1)  # recent week start date
        rwedt = rwsdt + datetime.timedelta(weeks=1) - datetime.timedelta(days=1)  # recent week end date
        pwsdt = rwsdt - datetime.timedelta(weeks=1)  # previous week start date
        pwedt = pwsdt + datetime.timedelta(weeks=1)  #previous week end date
        connection = pymysql.connect(read_default_file= os.path.join(BASE_DIR, 'db_frendy.cnf'))
        df = pd.read_sql(f"""
            select sale_order.opd_number, sale_order_item.product_id, product.sku, product.identifier, sale_order.created_at,
            sale_order_item.created_by_id, user.age, user.gender, sale_order_item.status, city.name as shipping_city,
            sale_order_item.amount, sale_order_item.mrp, sale_order_item.frendy_price, sale_order_item.quantity,
              sale_order_item.product_points, sale_order_item.root_category, sale_order_item.primary_category
            from sale_order_item 
            inner join sale_order on sale_order.id = sale_order_item.opd_master_id
            inner join product on product.id = sale_order_item.product_id
            inner join user on user.id = sale_order_item.created_by_id
            inner join city on city.id = sale_order.shipping_city_id
            where sale_order.status != 'Initiate' and (cast(sale_order.created_at as date) between '{str(pwsdt)}' and '{str(rwedt)}')"""
            , connection)

        # Strip spaces and convert to lowercase to avoid inconsistency
        df['root_category'] = df.root_category.transform(strip_lowercase)
        df['primary_category'] = df.primary_category.transform(strip_lowercase)

        # Addition of aggregated columns
        df['total_frendy'] = df['amount'] + (df['product_points'] * df['quantity'])
        df['savings'] = (df['mrp'] * df['quantity']) - df['total_frendy']
        df['earnings'] = (df['total_frendy'] - df['amount']) * 2

        consolidated_file = f"category_report_{str(rwsdt)}_{str(rwedt)}.xlsx"
        writer = pd.ExcelWriter(consolidated_file, engine="xlsxwriter")
        # previous week
        df_prev_wk = df[(df['created_at'] >= str(pwsdt)) & (df['created_at'] < str(pwedt))]
        # recent week
        df = df[(df['created_at'] >= str(rwsdt)) & (df['created_at'] < str(rwedt + datetime.timedelta(days=1)))]

        # Category
        categories = ['grocery', 'beauty', 'electronics', 'home & kitchen', 'fashion', 'stationery']
        for category in categories:
            df_category = df[df['root_category'] == category]
            # Previous week calculations
            df_prev_wk_cat = df_prev_wk[df_prev_wk['root_category'] == category]
            df_prev_wk_cat = df_prev_wk_cat[(df_prev_wk_cat['status'] != 'Returned') & (df_prev_wk_cat['status'] != 'Rto') & (df_prev_wk_cat['status'] != 'Canceled')]
            df_final_prev_wk = df_prev_wk_cat.groupby(['primary_category'])[
                'amount', 'product_points', 'savings', 'earnings'].sum().reset_index()
            orders_prev_wk = pd.DataFrame(
                df_prev_wk_cat.groupby(['primary_category'])['opd_number'].nunique()).reset_index()
            orders_prev_wk.rename(columns={'opd_number': 'order_count'}, inplace=True)
            quantity_prev_wk = pd.DataFrame(df_prev_wk_cat['primary_category'].value_counts()).reset_index()
            quantity_prev_wk.rename(columns={'primary_category': 'quantity',
                                             'index': 'primary_category'}, inplace=True)
            df_final_prev_wk = pd.merge(df_final_prev_wk, orders_prev_wk, on='primary_category')
            df_final_prev_wk = pd.merge(df_final_prev_wk, quantity_prev_wk, on='primary_category')
            last_rows_prev_wk = pd.DataFrame({'primary_category': ['Grand Total'],
                                              'amount': [df_final_prev_wk['amount'].sum()],
                                              'product_points': [df_final_prev_wk['product_points'].sum()],
                                              'savings': [df_final_prev_wk['savings'].sum()],
                                              'earnings': [df_final_prev_wk['earnings'].sum()],
                                              'order_count': [df_final_prev_wk['order_count'].sum()],
                                              'quantity': [df_final_prev_wk['quantity'].sum()],
                                              })
            df_final_prev_wk = pd.concat([df_final_prev_wk, last_rows_prev_wk], axis=0, sort=False)
            df_final_prev_wk = df_final_prev_wk.reset_index(drop=True)
            df_final_prev_wk['POV'] = round((df_final_prev_wk['product_points'] / df_final_prev_wk['amount']) * 100)
            df_final_prev_wk.rename(columns={'amount': 'prev_week_amount',
                                             'product_points': 'prev_week_product_points',
                                             'savings': 'prev_week_savings',
                                             'earnings': 'prev_week_earnings',
                                             'order_count': 'prev_week_order_count',
                                             'quantity': 'prev_week_quantity',
                                             'POV': 'prev_week_POV'}, inplace=True)

            # Logistic info
            logistic = df_category['status'].value_counts()
            logistic = pd.DataFrame(logistic).reset_index()
            logistic.rename(columns={'index': 'logistic_status',
                                     'status': ' order_count'}, inplace=True)

            df_category = df_category[(df_category['status'] != 'Returned') & (df_category['status'] != 'Rto') & (df_category['status'] != 'Canceled')]

            df_final = df_category.groupby(['primary_category'])[
                'amount', 'product_points', 'savings', 'earnings'].sum().reset_index()

            # Number of orders
            orders = pd.DataFrame(df_category.groupby(['primary_category'])['opd_number'].nunique()).reset_index()
            orders.rename(columns={'opd_number': 'order_count'}, inplace=True)

            # number of quantity
            quantity = pd.DataFrame(df_category['primary_category'].value_counts()).reset_index()
            quantity.rename(columns={'primary_category': 'quantity',
                                     'index': 'primary_category'}, inplace=True)
            df_final = pd.merge(df_final, orders, on='primary_category')
            df_final = pd.merge(df_final, quantity, on='primary_category')

            # Grand Total
            last_rows = pd.DataFrame({'primary_category': ['Grand Total'],
                                      'amount': [df_final['amount'].sum()],
                                      'product_points': [df_final['product_points'].sum()],
                                      'savings': [df_final['savings'].sum()],
                                      'earnings': [df_final['earnings'].sum()],
                                      'order_count': [df_final['order_count'].sum()],
                                      'quantity': [df_final['quantity'].sum()],
                                      })

            df_final = pd.concat([df_final, last_rows], axis=0, sort= False)
            df_final = df_final.reset_index(drop=True)
            df_final['POV'] = round((df_final['product_points'] / df_final['amount']) * 100)

            # Merge the previous week data to recent week data
            df_final = pd.merge(df_final, df_final_prev_wk, on='primary_category', how='outer')
            df_final = df_final[['primary_category', 'prev_week_amount', 'amount', 'prev_week_product_points', 'product_points', \
                 'prev_week_savings', 'savings', 'prev_week_earnings', 'earnings', 'prev_week_order_count', \
                 'order_count', 'prev_week_quantity', 'quantity', 'prev_week_POV', 'POV']]

            # Demograhpics
            demographic = df_category[['created_by_id', 'age', 'gender', 'shipping_city', 'amount']]
            demographic = demographic.drop_duplicates(subset='created_by_id')

            # Order count as per city name
            city_orders = pd.DataFrame(demographic['shipping_city'].value_counts()).reset_index()
            city_orders.rename(columns={'index': 'city',
                                        'shipping_city': 'orders_count'}, inplace=True)

            # amount and order count as per age interval and gender
            try:
                demographic['age_interval'] = pd.cut(demographic['age'], bins=7, precision=0)
                age_interval = pd.DataFrame(demographic.groupby(['gender'])['age_interval'].value_counts())
                age_interval.rename(columns={'age_interval': 'order_count'}, inplace=True)
                age_interval = age_interval.reset_index()
                amt_age_interval = pd.DataFrame(demographic.groupby(['age_interval'])['amount'].sum()).reset_index()
                amount_order_wrt_age_interval = pd.merge(age_interval, amt_age_interval, on='age_interval',
                                                         how="inner").sort_values(by=['gender', 'age_interval']).reset_index(drop=True)
            except ValueError:
                amount_order_wrt_age_interval = pd.DataFrame({0: []})

            # Top 20 SKU
            top_20_sku_quant = pd.DataFrame(df_category.groupby(['identifier'])['quantity', 'amount'].sum().sort_values(by='quantity', ascending=False).head(
                    20)).reset_index()
            top_20_sku_quant.rename(columns={'identifier': 'top_20_sku_quantitywise'}, inplace=True)

            top_20_sku_amt = pd.DataFrame(
                df_category.groupby(['identifier'])['amount', 'quantity'].sum().sort_values(by='amount', ascending=False).head(
                    20)).reset_index()
            top_20_sku_amt.rename(columns={'identifier': 'top_20_sku_amountwise',
                                           'amount': 'sku_amount'}, inplace=True)

            top_20_sku_value = df_category[['identifier', 'frendy_price']].sort_values(by='frendy_price',
                                                                                ascending=False).drop_duplicates(keep='first').head(20)
            top_20_sku_value = pd.merge(top_20_sku_value, pd.DataFrame(df_category.groupby(['identifer'])['quantity', 'amount'].sum()).reset_index(), on='sku')
            top_20_sku_value.rename(columns={'identifier': 'top_20_sku_value_wise'}, inplace=True)

            df_final['-'] = ''
            df_final = pd.concat([df_final, top_20_sku_quant], axis=1)
            df_final['--'] = ''
            df_final = pd.concat([df_final, top_20_sku_amt], axis=1)
            df_final[' -- '] = ''
            df_final = pd.concat([df_final, top_20_sku_value], axis=1)
            df_final['  --'] = ''
            df_final = pd.concat([df_final, logistic], axis=1)
            df_final['-- '] = ''
            df_final = pd.concat([df_final, city_orders], axis=1)
            df_final[' --   '] = ''
            df_final = pd.concat([df_final, amount_order_wrt_age_interval], axis=1)

            df_final.to_excel(writer, sheet_name=category, index=False)
        writer.save()

    except Exception as e:
        logging.exception("Exception thrown: ", e)
    finally:
        connection.close()