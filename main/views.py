from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def showmain(request):
    return render(request,'main/main.html')

def faq(request):
    return render(request,'main/faq.html')

def news(request):
    newss=News.objects.all()
    return render(request,'main/news.html',{'newss':newss})

def news_detail(request,id):
    news = get_object_or_404(News, pk = id)
    return render(request, 'main/news_detail.html',{'news':news})