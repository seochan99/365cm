from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save

#프로파일 모델 
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True,on_delete=models.CASCADE)    
    followings=models.ManyToManyField("self", related_name="followers", symmetrical=False)
    bio = models.TextField(max_length=20,null=True)
    profile_photo = models.ImageField(blank=True, null=True)


#팔로우 팔로잉
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
         Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  