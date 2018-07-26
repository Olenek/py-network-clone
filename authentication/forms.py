from django import forms
from main.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class FormReg(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class FormChangeProf(UserChangeForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

