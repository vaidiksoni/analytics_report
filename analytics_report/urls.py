from django.urls import path

from . import views

urlpatterns = [
                path('send_daily_report/', views.send_daily_report, name = 'send_daily_report'),
                # path('send_grocery_report/', views.send_grocery_report, name = 'send_grocery_report')

]