from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    path('', views.peek, name='home'),
    path('result/', views.res, name='result'),
    path('save/', views.save_result, name='save'),
]
