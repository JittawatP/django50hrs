from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Tracking(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    tracking = models.CharField(max_length=100,null=True,blank=True)
    other = models.TextField(null=True,blank=True)

    def __str__(self):
        return '{} - {} ({})'.format(self.name, self.tel, self.tracking)

class Product(models.Model):
    productId = models.IntegerField(default="0001")
    productName = models.CharField(max_length=100)
    categoryId = models.IntegerField()
    price = models.FloatField()
    detail = models.TextField(default="รายละเอียดสินค้า")

    def __str__(self):
        return '{} {} - {} ({}) - {}'.format(self.productId,self.productName, self.categoryId, self.price,self.detail)

class AskQA(models.Model):
    name = models.CharField(max_length=100, verbose_name='ชื่อ')
    email = models.CharField(max_length=100,null=True,blank=True,verbose_name='อีเมล')
    title = models.CharField(max_length=100,null=True,blank=True,verbose_name='หัวข้อ')
    detail = models.TextField(null=True,blank=True,verbose_name='รายละเอียด')
    answer = models.TextField(null=True,blank=True,verbose_name='ตอบคำถาม')

    def __str__(self):
        return '{} - {} ({}) - {}'.format(self.name, self.email, self.title, self.detail)


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author-image/', null=True,blank=True,default='default.png')

    def __str__(self):
        return self.author_name
    
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=280,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    images = models.ImageField(upload_to="post_image",null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    date_updated = models.DateTimeField(auto_now=True,null=True,blank=True)
    slug = models.SlugField(unique=True,max_length=100, null=True,blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

class Category(models.Model):
    category_name = models.CharField(max_length=255, default="หมวดหมู่ทั่วไป")
    category_detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name

class ProductName(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    detail = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to="product", null=True, blank=True)
    quantity = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    unit = models.CharField(max_length=255,default="-")
    image_url = models.CharField(max_length=255,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)

    def __str__(self): 
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photo',null=True,blank=True)
    usertype = models.CharField(max_length=100,default='member')
    interestin = models.CharField(max_length=100,null=True,blank=True)
    facebook = models.CharField(max_length=100,default='No Facebook')
    address = models.TextField(null=True,blank=True)
    tel = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user.username
    
class Discount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    percent = models.IntegerField(null=True,blank=True,default=10)
    active = models.BooleanField(default=False)

    
