import datetime
from analytics_report.utility_functions import *
import logging
from analytics_report.config import *
import os
from analytics.settings import EMAIL_HOST_USER

def daily_report_cron_job():
    try:
        print('INFO: CRON job for daily report has started at: ', datetime.datetime.now())
        required_date = datetime.date.today()
        daily_report(required_date=required_date)
        # Email parameters
        subject_daily_report = "Daily Report: Sale Performance"
        body_daily_report = "Please find the report dated: " + str(required_date)
        send_mail(subject=subject_daily_report, body=body_daily_report, sender=EMAIL_HOST_USER,
                  recipient=recipient_list, \
                  file_name=str(required_date) + '.csv')
        print('INFO: CRON job for daily report has ended at: ', datetime.datetime.now())

    except Exception as e:
        logging.exception("Exception thrown: ", e)
        print('Exception thrown at: ' + datetime.datetime.now() + ' as ', e)

    finally:
        if os.path.exists(str(required_date)+'.csv'):
            os.remove(str(required_date)+'.csv')



def category_weekly_report_cron_job():
    try:
        print('INFO: CRON job for weekly category report has started at: ', datetime.datetime.now())
        required_date = datetime.date.today()
        category_report(required_date=required_date)
        cwsdt = required_date - datetime.timedelta(required_date.weekday())
        pwsdt = cwsdt - datetime.timedelta(weeks=1)
        pwedt = pwsdt + datetime.timedelta(weeks=1) - datetime.timedelta(days=1)

        categories = ['grocery', 'beauty', 'electronics', 'home & kitchen', 'fashion', 'stationery']
        for category in categories:
            subject_category_report = "Category Weekly Report: " + category
            body_category_report = "Please find the report for the week: " + str(pwsdt) + " to " + str(pwedt)
            send_mail(subject= subject_category_report, body= body_category_report, sender= EMAIL_HOST_USER, recipient= recipient_list, \
                      file_name= category + '_' + str(pwsdt) + '_' + str(pwedt) + '.csv')
        print('INFO: CRON job for weekly category report has ended at: ', datetime.datetime.now())

    except Exception as e:
        logging.exception("Exception thrown: ", e)

    finally:
        for category in categories:
            if os.path.exists(category + '_' + str(pwsdt) + '_' + str(pwedt) + '.csv'):
                os.remove(category + '_' + str(pwsdt) + '_' + str(pwedt) + '.csv')
