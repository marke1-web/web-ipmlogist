from django.urls import path
from . import views
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
    ChangePasswordView,
)

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

urlpatterns += [
    path(
        'reset_password/',
        CustomPasswordResetView.as_view(),
        name='reset_password',
    ),
    path(
        'reset_password_sent/',
        CustomPasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset_password_complete/',
        CustomPasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
    path(
        'change-password/',
        ChangePasswordView.as_view(),
        name='change_password',
    ),
]
