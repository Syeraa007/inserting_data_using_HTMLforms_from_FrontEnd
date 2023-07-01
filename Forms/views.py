from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from Forms.models import *

def form_data(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pswd']
        # request.POST={'username':'un','password':'pswd'}
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
    if request.method=='POST':
        topic=request.POST['topic'] 
        Name=request.POST['names']
        Url=request.POST['urls']
        TO=Topic.objects.get(topic_name=topic)
        # request.POST={'topic':TO,'Name':'names','Url':'urls'}
        Webpage.objects.get_or_create(topic_name=TO,name=Name,url=Url)[0].save()
        return HttpResponse('Webpage added successfully')
    return render(request,'form_webpage.html')

def form_record(request):
    if request.method=='POST':
        topic=request.POST['topic'] 
        Name=request.POST['names']
        Date=request.POST['date']
        Author=request.POST['author']
        TO=Topic.objects.get(topic_name=topic)
        NO=Webpage.objects.get(name=Name)
        # request.POST={'Name':NO,'Date':'date','Author':'author'}
        AccessRecord.objects.get_or_create(name=NO,date=Date,author=Author)[0].save()
        
        return HttpResponse('Record added successfully')
    return render(request,'form_record.html')