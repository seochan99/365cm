from django.db import models
from django.contrib.auth.models import User 

# 퀴즈 모델 #
class Quiz(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  body = models.TextField()
  score = models.TextField(default="")

class Result(models.Model):
  id = models.AutoField(primary_key=True)
  flag = models.CharField(null = True, max_length=100)
  result_score = models.IntegerField(null = True)
  description = models.CharField(max_length=300)

class Select(models.Model):
  id = models.AutoField(primary_key=True)
  score = models.IntegerField()