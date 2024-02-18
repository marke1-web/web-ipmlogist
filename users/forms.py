from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(required=False)
    gender = forms.ChoiceField(choices=User.GENDER_CHOICES, required=False)
    phone_number = forms.CharField(max_length=11, required=True)
    car_number = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    username = forms.CharField(
        max_length=150, required=True
    )  # Добавление поля 'username'

    class Meta:
        model = User
        fields = (
            'username',  # Добавление 'username' в список полей
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'birth_date',
            'gender',
            'phone_number',
            'car_number',
        )
