from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm

# Create your views here.

class SignupView(CreateView):

    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):

    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = 'login'
