from django.shortcuts import render
# Create your views here.
from .calkwh import calculate as c


def peek(request):
    return render(request, 'calculator/peek.html')


def res(request):
    namelist = request.POST.getlist('name')
    numlist = request.POST.getlist('nums')
    recyclelist = []
    for pair in zip(namelist, numlist):
        recyclelist.append(pair)
    kwh = c(recyclelist)
    kgco2 = float(kwh) * 0.424
    tree = (kgco2 * 12) / (5.31 / 3000)
    context = {'kwh': kwh, 'co2': kgco2, 'tree': tree}
    return render(request, 'calculator/result.html', context)
