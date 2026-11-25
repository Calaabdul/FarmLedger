from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import SignupForm,  ProfileForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages

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


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)



class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('password-change-done')

class PasswordChangeDoneView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/password_change_done.html'