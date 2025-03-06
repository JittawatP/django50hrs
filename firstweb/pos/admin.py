from django.contrib import admin
from .models import *

class TableAdmin(admin.ModelAdmin):
    list_display = ("number", "qr_code")
admin.site.register(Table, TableAdmin) 

