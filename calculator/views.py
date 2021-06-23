from django.shortcuts import render

# Create your views here.


def peek(request):
    return render(request, 'peek.html')
