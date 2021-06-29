from django.shortcuts import render

# Create your views here.
def way(requset):
    return render(requset, 'way.html')