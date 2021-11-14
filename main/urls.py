from django.urls import path
from main import views
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('faq/', faq, name="faq"),
]