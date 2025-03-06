from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# def Sawatdee(request):
#     return HttpResponse('<h1>สวัสดีจ้า</h1>')

def AllTable(request):
    try:
        all_table = Table.objects.all()
    except Table.DoesNotExist:
        all_table = None

    context = {"all_table": all_table}

    return render(request,"pos/all_table.html", context)

