from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required #บังคับล็อกอิน

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

def Sawatdee(request):
    return HttpResponse('<h1>สวัสดีจ้า</h1>')

