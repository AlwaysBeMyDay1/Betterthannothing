from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .calkwh import calculate as c


def peek(request):
    return render(request, 'calculator/peek.html')


def res(request):
    namelist = request.POST.getlist('name')
    numlist = request.POST.getlist('nums')
    recyclelist = []
    for pair in zip(namelist, numlist):
        recyclelist.append(pair)
    kwh = round(c(recyclelist), 3)
    kgco2 = round(float(kwh) * 0.424, 3)
    tree = round((kgco2 * 12) / (5.31 * 3000), 3)
    context = {'kwh': kwh, 'co2': kgco2, 'tree': tree}
    return render(request, 'calculator/result.html', context)


@login_required(login_url='/common/login/')
def save_result(request):
    return redirect('home')
