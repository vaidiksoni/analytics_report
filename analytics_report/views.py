from django.shortcuts import render
from analytics_report.utility_functions import daily_report
import datetime
from django.core.mail import EmailMessage
from analytics_report.config import *
import os
import logging
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def send_daily_report(request):
    try:
        required_date = datetime.date.today()
        daily_report(required_date=required_date)
        mail = EmailMessage("Daily Report: Sale Performance","Please find the report dated: " + str(required_date),
                            from_user,
                            recipient_list)

        with open(str(required_date)+'.csv') as f:
            data = f.read()
            mail.attach(str(required_date)+'.csv',data,"text/csv")
        mail.send(fail_silently=False)
        return render(request, 'send_daily_report.html')
    except Exception as e:
        logging.exception("Exception thrown: ", e)

