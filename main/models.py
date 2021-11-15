from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="plan/", blank = True, null = True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)