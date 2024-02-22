from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from .forms import CustomUserCreationForm
from django.views import View
from django.views.generic import TemplateView


class ProfileView(TemplateView):

    template_name = 'users/profile.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().get(request)


class HomeView(TemplateView):
    template_name = 'users/home.html'

    def get(self, request):
        return super().get(request)


class RegisterView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'users/register.html', {'form': form})


class LoginView(View):

    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(
                request,
                'users/login.html',
                {'error': 'Неверное имя пользователя или пароль.'},
            )


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('home')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
