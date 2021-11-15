from django.urls import path
from main import views
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('faq/', faq, name="faq"),
    path('news/', news, name="news"),
    path('news_detail/<str:id>', news_detail, name="news_detail"),
    path('news_detail/<str:id>/create_comment', create_comment, name="create_comment"),
    path('news_detail/<str:news_id>/<str:comment_id>/update_comment', update_comment, name="update_comment"),
    path('news_detail/<str:news_id>/<str:comment_id>/delete_comment', delete_comment, name="delete_comment"),
]