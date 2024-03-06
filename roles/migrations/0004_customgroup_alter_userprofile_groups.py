# Generated by Django 4.2.10 on 2024-03-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0003_userprofile_role_permissions_delete_employees_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'verbose_name': 'Custom Group',
                'verbose_name_plural': 'Custom Groups',
            },
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(to='roles.customgroup'),
        ),
    ]
