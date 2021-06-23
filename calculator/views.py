from django.shortcuts import render
from .models import item
# Create your views here.


def peek(request):
    items_metal = item.objects.filter(type='metal')
    items_glass = item.objects.filter(type='glass')
    items_plastic = item.objects.filter(type='plastic')
    items_paper = item.objects.filter(type='paper')
    items_else = item.objects.filter(type='else')
    return render(request, 'peek.html', {'metal': items_metal,  'glass': items_glass, 'plastic': items_plastic, 'paper': items_paper, 'etc': items_else})
