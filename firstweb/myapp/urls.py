from django.urls import path
from .views import Home, Sawatdee, AboutUs, Contact


urlpatterns = [
    path('', Home, name='home'),
    path('aboutus', AboutUs, name='about-us'), #www.bankshop.com/aboutus
    path('contact', Contact, name='contact'), #www.bankshop.com/contact
    path('sawatdee', Sawatdee),

]
