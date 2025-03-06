from django.urls import path
# from .views import *
from . import views



urlpatterns = [
# path('',Sawatdee, name='home'),
path('tables/',views.AllTable, name='all-table'),
path('order/<int:table_id>/',views.OrderMenus, name='order-menu'),
]


