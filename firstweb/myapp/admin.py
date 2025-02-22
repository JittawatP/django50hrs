from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Author)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body",)
    list_display = ['id', 'title', 'images']
    list_editable = ['title']
admin.site.register(Post, PostAdmin)

admin.site.register(Tracking)
admin.site.register(Product)
admin.site.register(AskQA)

class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ("detail",)
    list_display = ['id', 'name', 'available']
    list_editable = ['name']
admin.site.register(ProductName, ProductAdmin)


class OrderAdmin(SummernoteModelAdmin):
    list_display = ['id','products']
admin.site.register(Order, OrderAdmin)

class TrackingOrderIDAdmin(SummernoteModelAdmin):
    list_display = ['id','tracking_order']
admin.site.register(TrackingOrderID,TrackingOrderIDAdmin)


admin.site.register(Category)

class UserProfile(SummernoteModelAdmin):
    list_display = ['id','user','usertype']
admin.site.register(Profile, UserProfile)

admin.site.register(Discount)

class CartAdmin(SummernoteModelAdmin):
    list_display = ['product_name']
admin.site.register(Cart, CartAdmin)

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['product_name']
admin.site.register(OrderProduct, OrderProductAdmin)

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']
admin.site.register(CartOrder, CartOrderAdmin)


