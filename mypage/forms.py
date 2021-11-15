from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignupForm(forms.Form):
    model = User

    def signup(self, request, user):
        profile = Profile()
        profile.user = user
        profile.save()
        user.save()
        return user

class ProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False) # 선택적으로 입력할 수 있음.
    class Meta:
        model = Profile
        fields = ['bio','profile_photo']