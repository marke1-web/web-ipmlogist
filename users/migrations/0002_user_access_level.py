# Generated by Django 4.2.10 on 2024-02-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='access_level',
            field=models.IntegerField(default=1),
        ),
    ]
