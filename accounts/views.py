from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from django.contrib.auth.views import LoginView

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


# class LogIn(LoginView):
#     template_name = 'accounts/login.html'
