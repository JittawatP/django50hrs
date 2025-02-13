from django.db import models

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
    name = models.CharField(max_length=100,null=True,blank=True, verbose_name='ชื่อ')
    email = models.CharField(max_length=100,null=True,blank=True,verbose_name='อีเมล')
    title = models.CharField(max_length=100,null=True,blank=True,verbose_name='หัวข้อ')
    detail = models.TextField(null=True,blank=True,verbose_name='รายละเอียด')

    def __str__(self):
        return '{} - {} ({}) - {}'.format(self.name, self.email, self.title, self.detail)


