from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import SetPasswordForm
from django.db.utils import IntegrityError
from django.db import IntegrityError
from django.contrib.auth.models import Group
from users.models import User, Role
from django.core.exceptions import ValidationError
from .utils import validate_password


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
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                error_message = 'Такая почта уже зарегистрирована. Пожалуйста, используйте другую почту.'
                return render(
                    request,
                    'users/register.html',
                    {'form': form, 'error_message': error_message},
                )

            if not validate_password(
                form.cleaned_data.get('password1'),
                form.cleaned_data.get('password2'),
            ):
                error_message = """Пароль должен содержать не менее 8 символов,
                                одну заглавную букву, одну строчную букву, одну цифру и один символ."""
                return render(
                    request,
                    'users/register.html',
                    {'form': form, 'error_message': error_message},
                )
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Пожалуйста, заполните форму корректно.'
            context = {'form': form, 'error_message': error_message}
            return render(request, 'users/register.html', context)


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


class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = 'registration/change_password.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, 'Вы успешно сменили пароль!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Пожалуйста, исправьте ошибку ниже.')
        return super().form_invalid(form)


class GetUserByEmailView(View):

    def get(self, request, *args, **kwargs):
        email = kwargs.get('email')
        try:
            user = User.objects.get(email=email)
            return HttpResponse(f'Найден пользователь: {user.username}')
        except User.DoesNotExist:
            return HttpResponse(
                f'Пользователь с адресом электронной почты "{email}" не найден'
            )


class AdminView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin_view.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['roles'] = Role.objects.all()
        context['groups'] = Group.objects.all()
        return context
