from django.urls import path
from . import views


urlpatterns = [
    path('', views.peek, name='home'),
]
