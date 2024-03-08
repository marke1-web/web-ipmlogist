from django.urls import path
from . import views
from .views import AdminPanelView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('create-user/', views.CreateUserView.as_view(), name='create_user'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('show-table/', views.AdminView.as_view(), name='show_table'),
    path('change-user/', AdminPanelView.as_view(), name='change_user'),
    path(
        'reset_password/',
        views.CustomPasswordResetView.as_view(),
        name='reset_password',
    ),
    path(
        'reset_password_sent/',
        views.CustomPasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        views.CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset_password_complete/',
        views.CustomPasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
    path(
        'change-password/',
        views.ChangePasswordView.as_view(),
        name='change_password',
    ),
]
