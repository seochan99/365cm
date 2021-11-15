from django.urls import path,re_path
from . import views 
from .views import *
from django.contrib.auth.decorators import login_required

app_name = "mypage"
urlpatterns = [
    path('mypage/<int:id>',views.mypage,name='mypage'),
    path('profile_update/', login_required(views.ProfileUpdateView.as_view()), name='profile_update'),
    path('<int:id>/follow',views.follow,name="follow"),
]
