from django.urls import path
#from .views import Home, Sawatdee, AboutUs, Contact, TrackingPage, Ask
from .views import *



urlpatterns = [
    path('', Home, name='home'), # name ข้างหลังคือไว้ใส่ใน {% url 'home' %}
    path('aboutus', AboutUs, name='about-us'), #www.bankshop.com/aboutus
    path('contact', Contact, name='contact'), #www.bankshop.com/contact
    path('tracking', TrackingPage, name='tracking'),
    path('ask', Ask, name='ask'),
    path('questions', Questions, name='questions'),
    path('answer/<int:askid>', Answer , name='answer'),
    path('blogs', Posts , name='post'),
    path('blog/<slug:slug>/', PostDetail , name='post-detail'),
    #Register and Login
    path('register', Register , name='register'),
    path('login', Login , name='login'),
    #products
    path('products', AllProduct , name='all-product'),
    path('discount', DiscountPage , name='discount'),
    path('sawatdee', Sawatdee),
    
]


