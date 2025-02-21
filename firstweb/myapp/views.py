from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required #บังคับล็อกอิน
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

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


def Sawatdee(request):
    return HttpResponse('<h1>สวัสดีจ้า</h1>')

