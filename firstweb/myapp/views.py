from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required #บังคับล็อกอิน
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
import string
import random



# Create your views here.
def Sawatdee(request):
    return HttpResponse('<h1>สวัสดีจ้า</h1>')

def Home(request):
    return render(request, 'myapp/home.html')

def AboutUs(request):
    return render(request, 'myapp/aboutus.html')

def Contact(request):
    return render(request, 'myapp/contact.html')

def TrackingPage(request):
    #tracks = ['ลุงวิศวกร - TD311T14','ลุงบูม - TD311T26','ลุงแบงค์ - TD311T79', 'ลุงปีเตอร์ - TD312T90']
    tracks = Tracking.objects.all() #objects.filter(name='สมชาย') สามารถใช้ search ได้
    context = {'tracks':tracks}
    return render(request, 'myapp/tracking.html', context)

def Ask(request):
    if request.method == 'POST':
        data = request.POST.copy()
        # print('DATA',data)
        name = data.get('name') # name = name
        email = data.get('email')
        title = data.get('title')
        detail = data.get('detail')
        # print(name,email,title,detail)

        new = AskQA()
        new.name = name
        new.email = email
        new.title = title
        new.detail = detail
        new.save()

    return render(request, 'myapp/ask.html')

@login_required
def Questions(request):
    questions = AskQA.objects.all() 
    context = {'questions':questions}
    return render(request, 'myapp/questions.html', context)

@login_required
def Answer(request,askid):
    # localhost:8000/answer/askid
    record = AskQA.objects.get(id=askid)

    if request.method == 'POST':
        data = request.POST.copy()
        # askid = data.get('askid')
        answer = data.get('answer')
        record.answer = answer
        record.save()

    context = {'record':record}

    return render(request, 'myapp/answer.html', context)


def Posts(request):
    posts = Post.objects.all().order_by('id').reverse()

    centext = {'posts':posts}
    return render(request, 'myapp/blogs.html',centext)


def PostDetail(request, slug):
    posts = Post.objects.all().order_by('id').reverse()[:3]
    try:
        single_post = get_object_or_404(Post, slug = slug)
        print("รายละเอียดบทความ", single_post)
    except Post.DoesNotExist:
        return render(request, 'myapp/home.html')
    
    context = {"single_post" : single_post,"posts": posts}
    return render(request, 'myapp/blog-detail.html', context)

def Register(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.copy()
        # print('DATA',data)
        name = data.get('name') # name = name
        email = data.get('email')
        password = data.get('password')

        check = User.objects.filter(username=email)
        # print('Check:', check)
        # print('Len', len(check))
        if len(check) == 0 :
            newuser = User()
            newuser.username = email
            newuser.first_name = name
            newuser.set_password(password)
            newuser.save()

            newprofile = Profile()
            newprofile.user = newuser
            newprofile.save()
            context['success'] = 'success'
        else:
            context['usertaken'] = 'usertaken'

        

    return render(request, 'myapp/register.html', context)
  
def Login(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.copy()
        # print('DATA',data)
        name = data.get('name') # name = name
        email = data.get('email')
        password = data.get('password')

        check = User.objects.filter(username=email)
        if len(check) == 0 :
            context['nouser'] = 'usertaken'
        else:
            try:
                user = authenticate(username=email,password=password)
                login(request,user)
                print('login completed')
                return redirect('questions')
            except:
                context['wrongpassword'] = 'wrongpassword'
                print('<br>fault login')

    return render(request, 'myapp/login.html', context)
  
def AllProduct(request):
    all_product = ProductName.objects.filter(available=True)
    print("All Product: ", all_product)
    context = {"all_product": all_product}

    return render(request,'myapp/all-product.html', context)

def DiscountPage(request):
    if request.user.discount.active == True:
       return redirect('all-product')

    context = {}
    if request.method == 'POST':
        data = request.POST.copy()
        # print('DATA',data)
        check = data.get('discount') 
        print("CHECK:", check)
        if check == 'check-true':
            user = User.objects.get(username=request.user.username)
            # เขียนแบบสองบรรทัดนี้ก็ได้
            # user.discount.active = True 
            # user.discount.save()
            discount = Discount.objects.get(user=user)
            discount.active = True
            discount.save()
            

            return redirect('all-product') # path('products', AllProduct , name='all-product'),

    return render(request, 'myapp/discount.html', context)

def RandomOrderID():
    ro_id = ""
    ro_id += random.choice(string.ascii_uppercase)
    ro_id += random.choice(string.ascii_uppercase)

    for i in range(8):
        ro_id += random.choice("0123456789")

    return ro_id

def ProductDetail(request, slug):
    RandomOrderID()
    product = ProductName.objects.get(slug=slug)
    context = {"product":product, "product_price": product.normal_price}
    if product.price1 > 0:
        price_1 = (product.price1*100)/product.normal_price

        context["price_1"] = 100 - int(price_1)
        context["product_price"] = product.price1
    
    if product.price2 > 0:
        price_2 = (product.price2*100) / product.normal_price

        context["price_2"] = 100 - int(price_2)
    
    if request.method == "POST":
        data = request.POST.copy()

        new_order = Order()
        new_order.products = product
        new_order.first_name = data.get("first_name")
        new_order.last_name = data.get("last_name")
        new_order.tel = data.get("tel")
        new_order.email = data.get("email")
        new_order.address = data.get("address")
        new_order.count = data.get("count")
        new_order.buyer_price = data.get("buyer_price")
        new_order.shipping_cost = data.get("shipping_cost")


        # file_image = request.FILES.get("upload_slip")  
        # ถ้าใส่ .get() จะไม่ติด error เนื่องจากถ้าไม่มีข้อมู,จะคืนค่า None
        try :
            file_image = request.FILES["upload_slip"]
            file_image_name = request.FILES["upload_slip"].name.replace(" ","")
            file_system_storage = FileSystemStorage()
            file_name = file_system_storage.save("product-slip/" + file_image_name, file_image)
            upload_file_url = "product-slip/" + file_image_name 
            # file_system_storage.url(file_name) ถ้าทำแบบนี้จะติด /media/ มาด้วย
            # ถ้าเขียนแบบด้านบนบรรทัดที่รับต้อง
            # new_order.slip = upload_file_url["6:"] ก็คือเอาตำแหน่งที่ 6 เป็นต้นไป /media/
            new_order.slip = upload_file_url
            # print("file_image_name: ",file_image_name)
            # print("file_name: ",file_name)
            # print("upload_file_url",upload_file_url)
        except:
            new_order.slip = "/default.png"
        new_order.save()

        # เพิ่่ม function random id
        try:
            tracking_id = TrackingOrderID.objects.all()  # ดึงข้อมูลทั้งหมดจากโมเดล TrackingOrderID
            while True:  # เริ่มลูปไม่รู้จบ
                order_ID = RandomOrderID()  # สร้าง random ID ใหม่โดยใช้ฟังก์ชัน RandomOrderID()
                for tid in tracking_id:  # วนลูปเพื่อเช็คทุกตัวที่มีใน tracking_id
                    if order_ID == tid.order_id:  # ถ้า order_ID ที่สร้างมาแล้วซ้ำกับ order_id ในฐานข้อมูล
                        continue  # ข้ามการทำงานในรอบนี้ (กลับไปเริ่มต้นการวนลูปใหม่)
                break  # ถ้าไม่ซ้ำ ก็จะออกจากลูป
        except:
            order_ID = RandomOrderID()  # หากเกิดข้อผิดพลาด (เช่น ไม่มีข้อมูลใน TrackingOrderID) ให้สร้าง order_ID ใหม่
        
        new_tracking_id = TrackingOrderID()
        new_tracking_id.tracking_order = new_order
        new_tracking_id.order_id = order_ID
        new_tracking_id.save()

        return redirect("tracking-order-id-page", order_ID)

    return render(request,'myapp/product-detail.html', context)

def TrackingOrderId(request, tid):
    tracking_id = TrackingOrderID.objects.get(order_id=tid).tracking_order
    buyer_price = tracking_id.buyer_price

    if buyer_price == int(buyer_price):
        buyer_price = int(buyer_price) 

    shipping_cost = tracking_id.shipping_cost
    if shipping_cost == int(shipping_cost):
        shipping_cost = int(shipping_cost)

    all_price = tracking_id.buyer_price + tracking_id.shipping_cost
    context = {
        "tracking_id":tracking_id,
        "buyer_price":buyer_price,
        "order_id":tid,
        "shipping_cost":shipping_cost,
        "all_price":all_price
        }
    
    return render(request,'myapp/tracking-order.html', context)


def AddToCart(request, pid):
    username = request.user.username
    user =User.objects.get(username=username)
    check = ProductName.objects.get(id=pid)

    try:
        new_cart = Cart.objects.get(user=user, product_id=str(pid))
        new_quantity = new_cart.quantity + 1
        new_cart.quantity = new_quantity
        calculate = new_cart.price * new_quantity
        new_cart.total = calculate
        new_cart.save()

        count = Cart.objects.filter(user=user)
        count = sum([c.quantity for c in count])

        updated_quantity = Profile.objects.get(user=user)
        updated_quantity.cart_quantity = count
        updated_quantity.save()

        return redirect('all-product')
    except:
        new_cart = Cart()
        new_cart.user = user
        new_cart.product_id = pid
        new_cart.product_name = check.name
        new_cart.price = int(check.normal_price)
        new_cart.quantity = 1
        calculate = int(check.normal_price) * 1
        new_cart.total = calculate
        new_cart.save()

        count = Cart.objects.filter(user=user)
        count = sum([c.quantity for c in count])
        updated_quantity = Profile.objects.get(user=user)
        updated_quantity.cart_quantity = count
        updated_quantity.save()

        return redirect('all-product')



def MyCart(request):
    username = request.user.username
    user = User.objects.get(username=username)
    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        product_id = data.get('product_id')


        try:
            item = Cart.objects.get(user=user, product_id=product_id)
            item.delete()
            context['status'] = 'delete'
            
        except Cart.DoesNotExist: 
            item = None

        count = Cart.objects.filter(user=user)
        count = sum([c.quantity for c in count])
        updated_quantity = Profile.objects.get(user=user)
        updated_quantity.cart_quantity = count
        updated_quantity.save()

    mycart = Cart.objects.filter(user=user)
    count = sum([c.quantity for c in mycart])
    total = sum([c.total for c in mycart])

    context['mycart'] = mycart
    context['count'] = count
    context['total'] = total
    
    return render(request, 'myapp/my-cart.html', context)


