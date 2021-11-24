from django.urls import path, include
from .views import *

app_name = "quiz"
urlpatterns = [
  path('main/', mainQuiz, name='mainQuiz'),
  path('<int:id>/', viewQuiz, name='viewQuiz'),
  path('select/<int:select_id>/<int:id>/', selectQuiz, name='selectQuiz'),
  path('select/next/<int:select_id>/<int:id>/', nextQuiz, name='nextQuiz'),
]