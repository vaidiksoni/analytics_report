from .models import SaleOrder, SaleOrderItem
from django.db.models import Sum
import datetime
import pandas as pd
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.db.models import Q
import calendar
import logging
from io import StringIO
import json
import boto3
from django.core.mail import EmailMessage
import pymysql.cursors
import os
from analytics.settings import BASE_DIR
# import xlswriter

def send_mail(subject, body, sender, recipient, file_name):
    """""Function to shoot email"""
    try:
        mail = EmailMessage(subject, body,
                            sender,
                            recipient)

        with open(file_name, 'rb') as f:
            data = f.read()
            mail.attach(file_name, data, "application/octet-stream")
        mail.send(fail_silently=False)
    except Exception as e:
        logging.exception("Exception thrown: ", e)


def upload_files_to_s3(credential_file_path, s3_file_path, file_to_upload):
    """
        Function to upload a file to a s3 bucket
    """
    try:
        try:
            with open(credential_file_path, "r") as f:
                aws_credentials = json.load(f)
            aws_access_key_id = aws_credentials['aws_access_key_id']
            aws_secret_access_key = aws_credentials['aws_secret_access_key']
            bucket_name = aws_credentials['bucket_name']
            s3_resource = boto3.resource("s3", aws_access_key_id=aws_access_key_id,
                                         aws_secret_access_key=aws_secret_access_key)
        except FileNotFoundError:
            #credentials.json not found, this script is for EC2 instance
            s3 = boto3.resource("s3")
            s3_bucket = s3.Bucket("frendy-ai")
            s3_bucket.upload_file(file_to_upload,s3_file_path)
            return True
        file_uploaded = False
        try:
            s3_resource.meta.client.upload_file(file_to_upload, bucket_name, s3_file_path)
            file_uploaded = True
        except Exception:
            file_uploaded = False
        return file_uploaded
    except Exception as e:
        logging.exception("Exception thrown: ", e)
        return False #for file being uploaded


def daily_report(required_date):
    """"returns gross, cancelled, net orders and star order along with the GMV for yesterday , day before yesterday, previous and current week"""

    # yd = yesterday
    try:
        yd_date = required_date - datetime.timedelta(1)
        gross_ord_count_yd = SaleOrder.objects.filter(created_at__date =yd_date).exclude(status__in=['Initiate']).count()
        cancelled_ord_count_yd = SaleOrder.objects.filter(created_at__date =yd_date).filter(status='Canceled').count()
        net_ord_count_yd = gross_ord_count_yd - cancelled_ord_count_yd
        star_ord_count_yd = SaleOrder.objects.filter(created_at__date= yd_date).filter(Q(keep_star_order= 1) | Q(extra_info__contains = {'activate_code':1})).count()
        gross_gmv_yd = SaleOrderItem.objects.filter(opd_master__created_at__date = yd_date).exclude(opd_master__status__in=['Initiate']).aggregate(total = Sum('amount'))['total']
        net_gmv_yd = SaleOrderItem.objects.filter(opd_master__created_at__date =yd_date).exclude(opd_master__status__in=['Canceled']).exclude(opd_master__status__in = ['Initiate']).aggregate(total = Sum('amount'))['total']
        if gross_ord_count_yd == 0:
            avg_gross_ord_value_yd = 0
            gross_gmv_yd = 0
        else:
            avg_gross_ord_value_yd = float(gross_gmv_yd)/float(gross_ord_count_yd)
        if net_ord_count_yd == 0:
            avg_net_ord_value_yd = 0
            net_gmv_yd = 0
        else:
            avg_net_ord_value_yd = float(net_gmv_yd)/float(net_ord_count_yd)

        # dyd = day before yesterday
        dyd_date = required_date - datetime.timedelta(2)
        gross_ord_count_dyd = SaleOrder.objects.filter(created_at__date= dyd_date).exclude(status__in=['Initiate']).count()
        cancelled_ord_count_dyd = SaleOrder.objects.filter(created_at__date= dyd_date).filter(status='Canceled').count()
        net_ord_count_dyd = gross_ord_count_dyd - cancelled_ord_count_dyd
        star_ord_count_dyd = SaleOrder.objects.filter(created_at__date=dyd_date).filter(Q(keep_star_order=1) | Q(extra_info__contains={'activate_code': 1})).count()
        gross_gmv_dyd = SaleOrderItem.objects.filter(opd_master__created_at__date=dyd_date).exclude(opd_master__status__in=['Initiate']).aggregate(total = Sum('amount'))['total']
        net_gmv_dyd = SaleOrderItem.objects.filter(opd_master__created_at__date=dyd_date).exclude(opd_master__status__in=['Canceled']).exclude(opd_master__status__in=['Initiate']).aggregate(total = Sum('amount'))['total']
        if gross_ord_count_dyd == 0:
            avg_gross_ord_value_dyd = 0
            gross_gmv_dyd = 0
        else:
            avg_gross_ord_value_dyd = float(gross_gmv_dyd)/float(gross_ord_count_dyd)

        if net_ord_count_dyd == 0:
            avg_net_ord_value_dyd =0
            net_gmv_dyd = 0
        else:
            avg_net_ord_value_dyd = float(net_gmv_dyd)/float(net_ord_count_dyd)

        #previous week
        # pwsdt = previous week start date, pwedt = previous week end date
        cwsdt = required_date - datetime.timedelta(required_date.weekday())
        pwsdt = cwsdt - datetime.timedelta(weeks=1)
        pwedt = pwsdt + datetime.timedelta(weeks=1)
        gross_ord_count_pw = SaleOrder.objects.filter(created_at__range=[pwsdt, pwedt]).exclude(status__in=['Initiate']).count()
        cancelled_ord_count_pw = SaleOrder.objects.filter(created_at__range=[pwsdt, pwedt]).filter(status='Canceled').count()
        net_ord_count_pw = gross_ord_count_pw - cancelled_ord_count_pw
        star_ord_count_pw = SaleOrder.objects.filter(created_at__range=[pwsdt, pwedt]).filter(Q(keep_star_order=1) | Q(extra_info__contains={'activate_code': 1})).count()
        gross_gmv_pw = SaleOrderItem.objects.filter(opd_master__created_at__range=[pwsdt, pwedt]).exclude(opd_master__status__in=['Initiate']).aggregate(total=Sum('amount'))['total']
        net_gmv_pw = SaleOrderItem.objects.filter(opd_master__created_at__range=[pwsdt, pwedt]).exclude(opd_master__status__in=['Canceled']).exclude(opd_master__status__in=['Initiate']).aggregate(total=Sum('amount'))['total']
        if gross_ord_count_pw == 0:
            avg_gross_ord_value_pw= 0
            gross_gmv_pw = 0
        else:
            avg_gross_ord_value_pw = float(gross_gmv_pw)/float(gross_ord_count_pw)
        if net_ord_count_pw == 0:
            avg_net_ord_value_pw = 0
            net_gmv_pw = 0
        else:
            avg_net_ord_value_pw = float(net_gmv_pw)/float(net_ord_count_pw)


        # current week
        # cwsdt = current week start date, cwedt = current week end date == yd_date
        cwedt = required_date
        if cwsdt == cwedt:
            gross_ord_count_cw = 0
            cancelled_ord_count_cw = 0
            net_ord_count_cw = gross_ord_count_cw - cancelled_ord_count_cw
            star_ord_count_cw = 0
            gross_gmv_cw = 0
            net_gmv_cw =0
            avg_gross_ord_value_cw = 0
            avg_net_ord_value_cw = 0

        else:
            gross_ord_count_cw = SaleOrder.objects.filter(created_at__range=[cwsdt, cwedt]).exclude(status__in=['Initiate']).count()
            cancelled_ord_count_cw = SaleOrder.objects.filter(created_at__range=[cwsdt, cwedt]).filter(status='Canceled').count()
            net_ord_count_cw = gross_ord_count_cw - cancelled_ord_count_cw
            star_ord_count_cw = SaleOrder.objects.filter(created_at__range=[cwsdt, cwedt]).filter(Q(keep_star_order=1) | Q(extra_info__contains={'activate_code': 1})).count()
            gross_gmv_cw =SaleOrderItem.objects.filter(opd_master__created_at__range=[cwsdt, cwedt]).exclude(opd_master__status__in=['Initiate']).aggregate(total=Sum('amount'))['total']
            net_gmv_cw =SaleOrderItem.objects.filter(opd_master__created_at__range=[cwsdt, cwedt]).exclude(opd_master__status__in=['Canceled']).exclude(opd_master__status__in=['Initiate']).aggregate(total=Sum('amount'))['total']
            if gross_ord_count_cw == 0:
                avg_gross_ord_value_cw = 0
                gross_gmv_cw = 0
            else:
                avg_gross_ord_value_cw = float(gross_gmv_cw)/float(gross_ord_count_cw)
            if net_ord_count_cw == 0:
                avg_net_ord_value_cw = 0
                net_gmv_cw = 0
            else:
                avg_net_ord_value_cw = float(net_gmv_cw)/float(net_ord_count_cw)


        # month to date
        # msdt = month starting date, medt =month end date
        msdt = required_date - timedelta(required_date.day - 1)
        medt = required_date
        if msdt == medt:
            gross_ord_count_mtd = int(0)
            cancelled_ord_count_mtd = int(0)
            net_ord_count_mtd = gross_ord_count_mtd - cancelled_ord_count_mtd
            star_ord_count_mtd = int(0)
            gross_gmv_mtd = int(0)
            net_gmv_mtd = int(0)
            avg_gross_ord_value_mtd = int(0)
            avg_net_ord_value_mtd = int(0)
        else:
            gross_ord_count_mtd = SaleOrder.objects.filter(created_at__range=[msdt, medt]).exclude(status__in=['Initiate']).count()
            cancelled_ord_count_mtd = SaleOrder.objects.filter(created_at__range=[msdt, medt]).filter(status='Canceled').count()
            net_ord_count_mtd = gross_ord_count_mtd - cancelled_ord_count_mtd
            star_ord_count_mtd = SaleOrder.objects.filter(created_at__range=[msdt, medt]).filter(Q(keep_star_order=1) | Q(extra_info__contains={'activate_code': 1})).count()
            gross_gmv_mtd = SaleOrderItem.objects.filter(opd_master__created_at__range=[msdt, medt]).exclude(opd_master__status__in=['Initiate']).aggregate(total=Sum('amount'))['total']
            net_gmv_mtd = SaleOrderItem.objects.filter(opd_master__created_at__range=[msdt, medt]).exclude(opd_master__status__in=['Canceled']).exclude(opd_master__status__in=['Initiate']).aggregate(total=Sum('amount'))['total']
            avg_gross_ord_value_mtd = float(gross_gmv_mtd) / float(gross_ord_count_mtd)
            avg_net_ord_value_mtd = float(net_gmv_mtd) / float(net_ord_count_mtd)


        # Previous month
        pmsdt = msdt - relativedelta(months=1)
        pmedt = msdt
        gross_ord_count_pm = SaleOrder.objects.filter(created_at__range=[pmsdt, pmedt]).exclude(status__in=['Initiate']).count()
        cancelled_ord_count_pm = SaleOrder.objects.filter(created_at__range=[pmsdt, pmedt]).filter(status='Canceled').count()
        net_ord_count_pm = gross_ord_count_pm - cancelled_ord_count_pm
        star_ord_count_pm = SaleOrder.objects.filter(created_at__range=[pmsdt, pmedt]).filter(Q(keep_star_order=1) | Q(extra_info__contains={'activate_code': 1})).count()
        gross_gmv_pm = SaleOrderItem.objects.filter(opd_master__created_at__range=[pmsdt, pmedt]).exclude(opd_master__status__in=['Initiate']).aggregate(total=Sum('amount'))['total']
        net_gmv_pm = SaleOrderItem.objects.filter(opd_master__created_at__range=[pmsdt, pmedt]).exclude(opd_master__status__in=['Canceled']).exclude(opd_master__status__in=['Initiate']).aggregate(total=Sum('amount'))['total']
        avg_gross_ord_value_pm = float(gross_gmv_pm) / float(gross_ord_count_pm)
        avg_net_ord_value_pm = float(net_gmv_pm) / float(net_ord_count_pm)

        # Total
        st_dt = datetime.date(2019,9,12)        #Launch Date
        gross_ord_count_total = SaleOrder.objects.filter(created_at__range=[st_dt, required_date]).exclude(status__in = ['Initiate']).count()
        cancelled_ord_count_total = SaleOrder.objects.filter(created_at__range=[st_dt, required_date]).filter(status='Canceled').count()
        net_ord_count_total = gross_ord_count_total - cancelled_ord_count_total
        star_ord_count_total = SaleOrder.objects.filter(created_at__range=[st_dt, required_date]).filter(Q(keep_star_order=1) | Q(extra_info__contains={'activate_code': 1})).count()
        gross_gmv_total = SaleOrderItem.objects.filter(opd_master__created_at__range=[st_dt, required_date]).exclude(opd_master__status__in=['Initiate']).aggregate(total=Sum('amount'))['total']
        net_gmv_total = SaleOrderItem.objects.filter(opd_master__created_at__range=[st_dt, required_date]).exclude(opd_master__status__in=['Canceled']).exclude(opd_master__status__in=['Initiate']).aggregate(total=Sum('amount'))['total']
        avg_gross_ord_value_total = float(gross_gmv_total) / float(gross_ord_count_total)
        avg_net_ord_value_total = float(net_gmv_total) / float(net_ord_count_total)

        # few column names
        prev_week = 'week: ' + str(pwsdt) + ' to ' + str(pwedt)
        current_week = 'week: ' + str(cwsdt) + ' to ' + str(cwedt)
        prev_month  = 'month: ' + calendar.month_name[int(str(pmsdt).split('-')[1])]
        current_month = 'mtd: ' + calendar.month_name[int(str(msdt).split('-')[1])]
        # dataframe creation
        df = pd.DataFrame({'Parameter' :['Gross Orders Count', 'Cancelled Orders Count', 'Net Orders Count', 'Star Orders Count', 'Gross GMV', 'Net GMV',\
                                               'Average Gross Orders Value', 'Average Net Orders value'],
                                dyd_date: [gross_ord_count_dyd, cancelled_ord_count_dyd, net_ord_count_dyd, star_ord_count_dyd, gross_gmv_dyd, net_gmv_dyd, \
                                      avg_gross_ord_value_dyd, avg_net_ord_value_dyd],
                                yd_date:[gross_ord_count_yd, cancelled_ord_count_yd, net_ord_count_yd, star_ord_count_yd, gross_gmv_yd, net_gmv_yd, \
                                        avg_gross_ord_value_yd, avg_net_ord_value_yd],

                               prev_week: [gross_ord_count_pw, cancelled_ord_count_pw, net_ord_count_pw, star_ord_count_pw, gross_gmv_pw, net_gmv_pw, \
                                         avg_gross_ord_value_pw, avg_net_ord_value_pw],
                               current_week: [gross_ord_count_cw, cancelled_ord_count_cw, net_ord_count_cw, star_ord_count_cw, gross_gmv_cw, net_gmv_cw, \
                                         avg_gross_ord_value_cw, avg_net_ord_value_cw],
                               current_month: [gross_ord_count_mtd, cancelled_ord_count_mtd, net_ord_count_mtd, star_ord_count_mtd, gross_gmv_mtd, \
                                                 net_gmv_mtd,avg_gross_ord_value_mtd, avg_net_ord_value_mtd],
                               prev_month: [gross_ord_count_pm, cancelled_ord_count_pm, net_ord_count_pm, star_ord_count_pm, gross_gmv_pm, net_gmv_pm,\
                                                  avg_gross_ord_value_pm, avg_net_ord_value_pm],
                                'total' : [gross_ord_count_total, cancelled_ord_count_total, net_ord_count_total, star_ord_count_total, gross_gmv_total, \
                                           net_gmv_total, avg_gross_ord_value_total, avg_net_ord_value_total]
                               })

        #columns for relative difference
        day_diff = []
        for i in range(8):
            if df[dyd_date][i] != 0:
                day_diff.append(float(df[yd_date][i] - df[dyd_date][i]) / float(df[dyd_date][i]))
            else:
                day_diff.append((df[yd_date][i] - df[dyd_date][i]) / 1)
        df['DOD_difference'] = day_diff
        week_diff = []
        for j in range(8):
            if df[prev_week][j] != 0:
                week_diff.append(float(df[current_week][j]) / float(df[prev_week][j]))
            else:
                week_diff.append(df[current_week][j])
        df['target_achieved_compared_to_last_week'] = week_diff         #(df[prev_week] - df[current_week]) / df[prev_week]

        # formatting
        for column in df.columns:
            if column != "Parameter":
                if column in ["DOD_difference", "target_achieved_compared_to_last_week"]:
                    df[column] = (df[column] * 100).astype(int).astype(str).apply(lambda row: row + "%")
                else:
                    df[column] = df[column].astype(int)
        df.loc[6:8,'target_achieved_compared_to_last_week'] = '-'
        df = df[['Parameter', dyd_date, yd_date, 'DOD_difference', current_week, prev_week, \
                 'target_achieved_compared_to_last_week', current_month, prev_month,  'total']]

        df.to_csv(str(required_date) + '.csv', index=False)  # export the DF to csv file

        ##SAVING THE DATAFRAME TO S3
        bucket = "frendy-autoreports"
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        s3_resource = boto3.resource('s3')
        s3_resource.Object(bucket, "daily_reports/" + str(required_date) + '.csv').put(Body=csv_buffer.getvalue())

        # CONSTRUCTING THE URL FOR THE CREATED FILE IN S3
        object_url = "https://{0}.s3.{1}.amazonaws.com/{2}/{3}.csv".format(bucket, "ap-south-1", "daily_reports",
                                                                           str(required_date))
        return object_url
    except Exception as e:
        logging.exception("Exception thrown: ",e)

    finally:
        pass


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