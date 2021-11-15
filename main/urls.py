from django.urls import path
from main import views
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('faq/', faq, name="faq"),
    path('news/', news, name="news"),
    path('news_detail/<str:id>', news_detail, name="news_detail"),
]