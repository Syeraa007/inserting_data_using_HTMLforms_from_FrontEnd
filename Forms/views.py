from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from Forms.models import *

def form_data(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pswd']
        Form.objects.get_or_create(UserName=username,PassWord=password)[0].save()
        return HttpResponse('Data is inserted successfully',request.POST)
    return render(request,'form_data.html')

def form_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']
        Topic.objects.get_or_create(topic_name=topic)[0].save()
        return HttpResponse('Topic inserted perfectly')
    return render(request,'form_topic.html')

def form_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        topic=request.POST['topic'] 
        Name=request.POST.get('names')
        Url=request.POST.get('urls')
        TO=Topic.objects.get(topic_name=topic)
        Webpage.objects.get_or_create(topic_name=TO,name=Name,url=Url)[0].save()
        return HttpResponse('Webpage added successfully')
    return render(request,'form_webpage.html',d)

def form_record(request):
    LTO=Topic.objects.all()
    LWO=Webpage.objects.all()
    d={'LTO':LTO,'LWO':LWO}
    if request.method=='POST':
        Name=request.POST.get('names')
        Date=request.POST.get('date')
        Author=request.POST.get('author')
        NO=Webpage.objects.get(name=Name)
        AccessRecord.objects.get_or_create(name=NO,date=Date,author=Author)[0].save()
        return HttpResponse('Record added successfully')
    return render(request,'form_record.html',d)

def retrieve_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MST=request.POST.getlist('topic')
        WEQS=Webpage.objects.none()
        for wo in MST:
            WEQS=WEQS|Webpage.objects.filter(topic_name=wo)
        d1={'WEQS':WEQS}
        return render(request,'webpage_result.html',d1)
    return render(request,'retrieve_webpage.html',d)

def webpage_result(request):
    return render(request,'webpage_result.html')

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return  render(request,'checkbox.html',d)
    