from django.db import models
from users.models import User


class JournalContractType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class JournalContract(models.Model):
    """Журнал договоров"""
    journal_type = models.ForeignKey(JournalContractType, on_delete=models.CASCADE)  # тип журнала
    date = models.DateField()  # дата
    number = models.CharField(max_length=256)  # номер
    customer = models.CharField(max_length=256)  # заказчик
    contractor = models.CharField(max_length=256)  # исполнитель
    contract_type = models.CharField(max_length=256)  # вид договора
    currency = models.CharField(max_length=32)  # валюта
    status = models.CharField(max_length=64)  # статус
    status_date = models.DateField()  # дата статуса
    sbt = models.CharField(max_length=64)  # принят по sbt

    def __str__(self):
        return f"Запись {self.id}"

    class Meta:
        ordering = ["date"]
