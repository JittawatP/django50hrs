from django.urls import path
#from .views import Home, Sawatdee, AboutUs, Contact, TrackingPage, Ask
from .views import *



urlpatterns = [
    path('sawatdee', Sawatdee),
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
    path('product/<slug:slug>', ProductDetail , name='product-detail'),
    path('tracking-order/<str:tid>', TrackingOrderId, name= 'tracking-order-id-page'),
    # EP17 Cart
    path('add-cart/<str:pid>', AddToCart, name='add-to-cart'),
    path('cart/', MyCart , name='my-cart'),
    # End EP17
    # EP18
    path('edit-cart/', MyCartEdit , name='my-cart-edit'),
    path('checkout/', Checkout , name='checkout'),
    # End EP18
    # EP19
    path('orders/', CartOrderProduct , name='cart-order-product'),
    path('upload-slip/<str:order_id>/', UploadSlipOrder , name='upload-slip-order'),
    path('customer-all-order/', CustomerAllOrder , name='-ordcustomer-aller'),  
    path('update-status/<str:order_id>/<str:status>/', UpdatePaid , name='update-status'),  
    path('update-tracking/<str:order_id>/', CartOrderUpdateTracking , name='cart-order-update-tracking'),      
    path('my-order/<str:order_id>/', MyOrder , name='my-order'),      
    # End EP19
    # EP20 Rental 1
    path('machines/', AllMachine , name='all-machines-page'), 
    path('machine/<int:machine_id>/', MachineDetail , name='machine-detail-page'),          
    # End EP20
    # EP21 Rental 2
    path('machine/<int:machine_id>/reserve', MakeREservation , name='make-reservation-page'),          
    path('wishlist/', Wishlists , name='wishlist-page'),  
    path('wishlist/add/<int:product_id>', AddtoWishlist , name='add-to-wishlist-page'),  
    path('wishlist/remove/<int:item_id>', RemovefromWishlist , name='remove-from-wishlist-page'),  

    # End EP21

    
]


