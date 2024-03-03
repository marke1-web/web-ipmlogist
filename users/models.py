from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    """Модель для хранения ролей пользователей"""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """Собственная модель пользователя"""

    GENDER_CHOICES = (
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    )

    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True
    )
    phone_number = models.CharField(max_length=11)
    car_number = models.CharField(max_length=20)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.username
