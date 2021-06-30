from django.shortcuts import render

# Create your views here.


def info(request):
    return render(request, 'challenge/ch_info.html')


def home(request):
    return render(request, 'challenge/chhome.html')
