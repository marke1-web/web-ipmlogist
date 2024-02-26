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
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'birth_date',
            'gender',
            'phone_number',
            'car_number',
        )

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['email']  # Устанавливаем username равным email
        if commit:
            user.save()
        return user
