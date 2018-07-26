from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from authentication import forms as f
# Create your views here.


def confirm(request):
    return render(request, template_name='confirm.html')


def reset_password(request):
    return render(request, template_name='reset_password.html')


def log_out(request):
    logout(request)
    return render(request, template_name='base.html')


def log_in(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, template_name='index.html', context={'request': request})
    return render(request, template_name='login.html')


def register(request):
    if request.method == 'POST':
        form = f.FormReg(request.POST)
        form.avatar = None
        if form.is_valid():
            form.save()
        return render(request, template_name='reg.html', context={'form': form, 'request':request})
    return render(request, template_name='reg.html')


@login_required(login_url="/login/")
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        print(request.POST)
        if form.is_valid():
            update_session_auth_hash(request, form.save())
        return render(request, template_name='change_password.html', context={'request': request, 'form': form})
    return render(request, template_name='change_password.html')


@login_required(login_url="/login/")
def userprofile(request):
    if request.method == 'POST':
        form = f.FormChangeProf(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return render(request, template_name='profile.html', context={'request': request, 'form': form})
    return render(request, template_name='profile.html', context={'request': request})
