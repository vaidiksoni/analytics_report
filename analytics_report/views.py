from django.shortcuts import render
import pymysql
import MySQLdb
import pandas as pd
from .models import *
# from django.http import *
# Create your views here.


def return_sale_order_item(request):
    sale_ord_obj = SaleOrderItem.objects.all()[:10]
    context_ord = {'sale_ord_obj': sale_ord_obj}
    df = pd.DataFrame(sale_ord_obj.values())
    # df.to_csv("delete_me.csv",index=False)
    return render(request, 'sale_ord.html', context_ord)

