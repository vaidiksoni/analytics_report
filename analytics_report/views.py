from django.shortcuts import render
from analytics_report.utility_functions import *
import datetime

from analytics_report.config import *
import os
import logging
from analytics.settings import EMAIL_HOST_USER
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def send_daily_report(request):
    try:
        required_date = datetime.date.today()
        daily_report(required_date=required_date)
        # Email parameters
        subject_daily_report = "Daily Report: Sale Performance"
        body_daily_report = "Please find the report dated: " + str(required_date)
        daily_report_file = str(required_date) + '.csv'
        send_mail(subject=subject_daily_report, body=body_daily_report, sender=EMAIL_HOST_USER, recipient=recipient_dict['daily_report'], \
                  file_name=daily_report_file)
        return render(request, 'send_daily_report.html')

    except Exception as e:
        logging.exception("Exception thrown: ", e)

    finally:
        if os.path.exists(daily_report_file):
            os.remove(daily_report_file)



def send_category_weekly_report(request):
    try:
        required_date = datetime.date.today()
        category_report(required_date=required_date)
        cwsdt = required_date - datetime.timedelta(required_date.weekday())
        pwsdt = cwsdt - datetime.timedelta(weeks=1)
        pwedt = pwsdt + datetime.timedelta(weeks=1) - datetime.timedelta(days=1)
        # Email Parameters
        consolidated_file = "category_report_" + str(pwsdt) + "_" + str(pwedt) + ".xlsx"
        subject_category_report = "Category Weekly Report For Week "+ str(pwsdt.isocalendar()[1]) +":"+ " [" +str(pwsdt)\
                                  + " - " + str(pwedt) + "]"
        body_category_report = "Please find the report for the week: " + str(pwsdt) + " to " + str(pwedt)
        send_mail(subject= subject_category_report, body= body_category_report, sender= EMAIL_HOST_USER, recipient= recipient_dict['category_report'], \
                  file_name= consolidated_file)
        return render(request, 'send_category_report.html')

    except Exception as e:
        logging.exception("Exception thrown: ", e)
    finally:
        if os.path.exists(consolidated_file):
            os.remove(consolidated_file)

