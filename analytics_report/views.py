from django.shortcuts import render
from analytics_report.utility_functions import daily_report
import datetime
from django.core.mail import EmailMessage

# Create your views here.
import os
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def send_mail(request):
    try:
        required_date = datetime.date.today()
        daily_report(required_date=required_date)
        mail = EmailMessage("Daily Report: Sale Performance","Please find the report.","vaidik.s@frendy.in",
                            ["kaumil.t@frendy.in"])

        with open(str(required_date)+'.csv') as f:
            data = f.read()
            mail.attach(str(required_date)+'.csv',data,"text/csv")
        mail.send(fail_silently=False)
        return render(request, 'send_mail.html')
    except Exception as e:
        logging.exception("Exception thrown: ", e)

