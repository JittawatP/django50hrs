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

admin.site.register(Category)