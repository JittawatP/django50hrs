from django.db import models
from taggit.managers import TaggableManager

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

