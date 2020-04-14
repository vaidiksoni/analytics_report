import datetime
from analytics_report.utility_functions import daily_report
import logging
from django.core.mail import EmailMessage
from analytics_report.config import *

def daily_report_cron_job():
    try:
        print('INFO: CRON job has started at: ', datetime.datetime.now())
        required_date = datetime.date.today()
        daily_report(required_date=required_date)
        mail = EmailMessage("Daily Report: Sale Performance","Please find the report dated: " + str(required_date),
                            from_user,
                            recipient_list)

        with open(str(required_date)+'.csv') as f:
            data = f.read()
            mail.attach(str(required_date)+'.csv',data,"text/csv")
        mail.send(fail_silently=False)
        print('INFO: CRON job has ended at: ', datetime.datetime.now())

    except Exception as e:
        logging.exception("Exception thrown: ", e)
        print('Exception thrown at: ' + datetime.datetime.now() + ' as ', e)
