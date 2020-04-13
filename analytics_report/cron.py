import datetime
from analytics_report.utility_functions import daily_report
import logging
from django.core.mail import EmailMessage

def daily_report_cron_job():
    try:
        print('CRON job has started')
        required_date = datetime.date.today()
        daily_report(required_date=required_date)
        mail = EmailMessage("Daily Report: Sale Performance","Please find the report dated: " + str(required_date),
                            "vaidik.s@frendy.in",
                            ["nishi.g@frendy.in","gowrav@frendy.in"])

        with open(str(required_date)+'.csv') as f:
            data = f.read()
            mail.attach(str(required_date)+'.csv',data,"text/csv")
        mail.send(fail_silently=False)
        print('CRON job has ended')

    except Exception as e:
        logging.exception("Exception thrown: ", e)
