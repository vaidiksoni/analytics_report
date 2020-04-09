import datetime
from analytics_report.utility_functions import daily_report
import logging
from django.core.mail import EmailMessage

def daily_report_cron_job():
      try:
        required_date = datetime.date.today()
        daily_report(required_date=required_date)
        mail = EmailMessage("Daily Report: Sale Performance","Please find the report.","vaidik.s@frendy.in",
                            ["kaumil.t@frendy.in"])

        with open(str(required_date)+'.csv') as f:
            data = f.read()
            mail.attach(str(required_date)+'.csv',data,"text/csv")
        mail.send(fail_silently=False)


      except Exception as e:
            logging.exception("Exception thrown: ", e)
