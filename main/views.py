from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Count

# Create your views here.
def showmain(request):
    return render(request,'main/main.html')

def showmains(request):
    return render(request,'main/mains.html')

def faq(request):
    return render(request,'main/faq.html')

def news(request):
    newss=News.objects.all()
    return render(request,'main/news.html',{'newss':newss})

def news_detail(request,id):
    news = get_object_or_404(News, pk = id)
    comments = news.comments.all().order_by('-created_at')
    cnt = 0
    if Comments.objects.all():
        cnt = list(Comments.objects.values('news').annotate(Count('news')))[0]
        cnt = cnt['news__count']
    return render(request, 'main/news_detail.html',{'news':news, 'comments': comments, 'cnt': cnt})

def create_comment(request, id):
    if request.method == "POST":
        news = get_object_or_404(News, pk=id)
        current_user = request.user
        content = request.POST.get('content')
        Comments.objects.create(news=news, content=content, writer=current_user)
    return redirect('main:news_detail', id)

def update_comment(request, news_id, comment_id):
    news = get_object_or_404(News, pk=news_id)
    comment = get_object_or_404(Comments, pk=comment_id)
    if request.method=="POST":
        comment.content = request.POST['content']
        comment.save()
        return redirect('main:news_detail', news.pk)
    context = {
        'news': news,
        'comment': comment
    }
    return render(request, 'main/comments_update.html', context)

def delete_comment(request, news_id, comment_id):
    comment = get_object_or_404(Comments, pk=comment_id)
    comment.delete()
    return redirect('main:news_detail', news_id)

def mainnews(request):
    newss=News.objects.all()
    return render(request,'main/main.html',{'newss':newss})