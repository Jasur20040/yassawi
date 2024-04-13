from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import AbstractUser
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import ListView
import datetime
from .models import *
from .forms import *


def index(request):
    kyrs = Kyrs.objects.all()
    return render(request, 'main/index.html', {'kyrs': kyrs})


def Kyrss (request):
    kyrs = Kyrs.objects.all()
    return render(request, 'main/course.html', {'kyrs': kyrs})

class AddKyrs(View):
    def post(self, request, pk):
        form = KyrsForm(request.POST, request.FILES)
        user = User.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()
        return redirect('index')

class User1(View):
    def get(self, request, slug):
        kyrs = Kyrs.objects.filter(user__id=slug)
        user = User.objects.get(id=slug)
        form = KyrsForm()
        return render(request, 'main/user.html', {'form': form, 'kyrs': kyrs, 'user': user, })

def sign(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname, email, password)
        my_user.save()
        return redirect('logins')
    return render(request, 'main/signup.html')


def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pas = request.POST.get('pass')
        user = authenticate(request, username=username, password=pas)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Geçersiz kullanıcı adı veya şifre')
            return render(request, 'main/login.html')

    return render(request, 'main/login.html')


def log_out(request):
    logout(request)
    return redirect('logins')