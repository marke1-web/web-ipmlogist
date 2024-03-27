# Generated by Django 5.0.3 on 2024-03-20 13:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='documentcontract',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создавший пользователь'),
        ),
        migrations.AddField(
            model_name='employee',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_app.company', verbose_name='ID компании'),
        ),
        migrations.AddField(
            model_name='documentcontract',
            name='contractor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractor', to='file_app.employee', verbose_name='Исполнитель'),
        ),
        migrations.AddField(
            model_name='documentcontract',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='file_app.employee', verbose_name='Заказчик'),
        ),
    ]
