from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.models import User

from django.db import models

from django.views.generic import detail
from django.views.generic.detail import DetailView
from django.views import View

from donation.models import Donate
from .forms import  ProfileForm

from django.shortcuts import render,get_object_or_404, redirect

# 메인앱의 모델에서 스토리,음악,일러스트 가져오기 
from main.models import *

#마이페이지 
def mypage(request,id):
    user = get_object_or_404(User,pk=id)
    context = {
        'user':user,
        'my_donation' : Donate.objects.filter(donate_member=user),
        'profile_user':DetailView.model,
        'followings':user.profile.followings.all(), 
        'followers':user.profile.followers.all(),
    }
    DetailView.context_object_name='profile_user'
    DetailView.model = User 
    DetailView.template_name = 'mypage/mypage.html'

    return render(request,"mypage/mypage.html",context)


#프로파일 업데이트 
class ProfileView(DetailView):
    context_object_name = 'profile_user' # model로 지정해준 User모델에 대한 객체와 로그인한 사용자랑 명칭이 겹쳐버리기 때문에 이를 지정함
    model = User
    template_name = 'mypage/mypage.html'
    


class ProfileUpdateView(View):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)  # 로그인중인 사용자 객체를 얻어옴
        if hasattr(user, 'profile'):  # user가 profile을 가지고 있으면 True, 없으면 False (회원가입을 한다고 profile을 가지고 있진 않으므로)
            profile = user.profile
            profile_form = ProfileForm(initial={
                'bio': profile.bio,
                'profile_photo': profile.profile_photo,
            })
        else:
            profile_form = ProfileForm()

        return render(request, 'mypage/profile_update.html', { "profile_form": profile_form})
        
    def post(self, request):
        u = User.objects.get(id=request.user.pk)        

        if hasattr(u, 'profile'):
            profile = u.profile
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile) # 기존꺼 가져와 수정 
        else:
            profile_form = ProfileForm(request.POST, request.FILES) # 새로 만드는 것

        # Profile 폼
        if profile_form.is_valid():
            profile = profile_form.save(commit=False) # 기존의 것을 가져와 수정하는 경우가 아닌 새로 만든 경우 user를 지정해야 함
            profile.user = u
            profile.save()

        return redirect('mypage:mypage',u.id)



#팔로우 기능 
def follow(request,id):
    user=request.user
    followed_user=get_object_or_404(User,pk=id) 
    is_follower=user.profile in followed_user.profile.followers.all() 
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile) 
    return redirect('mypage:mypage', followed_user.id)
