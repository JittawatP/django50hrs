from django.urls import path
#from .views import Home, Sawatdee, AboutUs, Contact, TrackingPage, Ask
from .views import *


urlpatterns = [
    path('', Home, name='home'), # name ข้างหลังคือไว้ใส่ใน {% url 'home' %}
    path('aboutus', AboutUs, name='about-us'), #www.bankshop.com/aboutus
    path('contact', Contact, name='contact'), #www.bankshop.com/contact
    path('tracking', TrackingPage, name='tracking'),
    path('ask', Ask, name='ask'),
    path('sawatdee', Sawatdee),

]
