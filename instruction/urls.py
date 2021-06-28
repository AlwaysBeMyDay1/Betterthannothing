from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'instruction'

urlpatterns = [
    path('way/', views.way, name='way'),
]