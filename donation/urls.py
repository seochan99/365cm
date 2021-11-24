from django.urls import path
from donation import views
from .views import *


app_name = "donation"
urlpatterns = [
    path('donate/', donate, name="donate"),
    path('donate_detail/<int:id>', donate_detail, name="donate_detail"),
    path('donate_new/', donate_new, name="donate_new"),
    path('donate_create/', donate_create, name="donate_create"),
    path('donate_edit/<int:id>', donate_edit, name="donate_edit"),
    path('donate_update/<int:id>', donate_update, name="donate_update"),
    path('donate_delete/<int:id>', donate_delete, name="donate_delete"),
    path('donate_complete', donate_complete, name="donate_complete"),
]