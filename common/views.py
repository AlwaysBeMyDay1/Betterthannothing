from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from .forms import *


def test(request):
    return render(request, 'common/test.html')


def logout_(request):
    logout(request)
    return redirect('test')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('test')
    else:
        form = RegisterForm()
        return render(request, 'common/register.html', {'form': form})
