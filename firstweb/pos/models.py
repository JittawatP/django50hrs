from django.db import models
import qrcode 
from django.conf import settings
import os

class Table(models.Model):
    number = models.IntegerField(unique=True)
    qr_code = models.ImageField(upload_to="qr-codes/", null=True, blank=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.generate_qr_code()

    def generate_qr_code(self):
        url = f"{settings.SITE_URL}/pos/order/{self.id}/"
        qr = qrcode.make(url)
        qr_code_path = f"qr-codes/table_{self.id}.png"
        qr.save(os.path.join(settings.MEDIA_ROOT, qr_code_path))
        self.qr_code = qr_code_path
        super().save()

    def __str__(self):
        return f"{self.number}"
    
class Category(models.Model):
    name = models.CharField(max_length=150)
    images = models.ImageField(upload_to="category-images/")

    def __str__(self):
        return f"{self.name}"

class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField(default=0)
    price_discount = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    # EP24
    is_new = models.BooleanField(default=False)
    is_promotion = models.BooleanField(default=False)
    # End EP24
    images = models.ImageField(upload_to="menu-images/")
    unit = models.CharField(max_length=20, default="แก้ว")

    def __str__(self):
        return self.name

class OrderMenu(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu = models.ManyToManyField(Menu)
    total_buyer_price = models.FloatField(default=0)
    count = models.IntegerField(default=1)
    vat = models.FloatField(default=0)
    final_price_with_vat = models.FloatField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)
    # EP24 แก้จาก TimeField เป็น DateTimeField
    order_time = models.DateTimeField(auto_now_add=True)
    # End EP24

    status = models.CharField(
        max_length=20, 
        choices=[("pendind","รอดำเนินการ"),
                 ("in_process","อยู่ระหว่างดพเนินการ"),
                 ("completed","เสร็จเรียบร้อย"),
        ],
    )

    def __str__(self):
        return f"{self.table.number} {self.menu.name}"

class OrderMenuItem(models.Model):
    # ถ้า order_menu ไม่เพิ่ม related_name = "order_items"
    # เวลาจะเรียกย้อนจาก OrderMenu มา OrderMenuItem ต้องใช้ {% order_menu.ordermenuitem_set.all %}
    # ถ้าใช้ related_name จะเรียก {% order_menu.order_item.all %}   ในหน้า html 
    order_menu = models.ForeignKey(OrderMenu, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    count = models.IntegerField()
    item_total = models.FloatField(default=0)

    def __str__(self):
        return f"{self.order_menu.table.number} {self.menu.name}"
    
class Promotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount_percentage = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    images = models.ImageField(upload_to='promotions/')
    applicable_menu = models.ManyToManyField(Menu)

    def __str__(self):
        return self.name
    

