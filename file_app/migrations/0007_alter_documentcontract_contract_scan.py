# Generated by Django 4.2.10 on 2024-03-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0006_documentcontract_delete_journalcontract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentcontract',
            name='contract_scan',
            field=models.FileField(blank=True, upload_to='contract_scan/%Y%m/', verbose_name='Скан договора'),
        ),
    ]
