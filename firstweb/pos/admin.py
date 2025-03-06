from django.contrib import admin
from .models import *

class TableAdmin(admin.ModelAdmin):
    list_display = ["number", "qr_code"]
admin.site.register(Table, TableAdmin) 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
admin.site.register(Category, CategoryAdmin) 

class MenuAdmin(admin.ModelAdmin):
    list_display = ["name","description"]
admin.site.register(Menu, MenuAdmin) 

class OrderMenuAdmin(admin.ModelAdmin):
    list_display = ["table"]
admin.site.register(OrderMenu, OrderMenuAdmin) 

class OrderMenuItemAdmin(admin.ModelAdmin):
    list_display = ["order_menu"]
admin.site.register(OrderMenuItem, OrderMenuItemAdmin) 
