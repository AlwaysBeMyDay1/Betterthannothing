from django.urls import path
from . import views

app_name = 'challenge'

urlpatterns = [
    path('info', views.info, name='ch_info'),
]
