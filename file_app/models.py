from django.db import models
from users.models import User


class Company(models.Model):
    """Модель для компаний исполнителей, заказчиков и контрагентов"""
    company_name = models.CharField(unique=True, blank=False, max_length=255, verbose_name="Название компании")
    tax_identification_number = models.CharField(unique=True, max_length=12, blank=False, verbose_name="ИНН")
    is_counterparty = models.BooleanField(default=False, blank=False, verbose_name="Является контрагентом")
    is_contractor = models.BooleanField(default=False, blank=False, verbose_name="Является исполнителем")

    def __str__(self):  # название документа
        return self.company_name

    class Meta:
        verbose_name = "Компания"  # человеческое название модели


class Employee(models.Model):
    """Модель для сотрудников компаний"""
    full_name = models.CharField(blank=False, max_length=256, verbose_name="ФИО")
    phone = models.CharField(blank=False, max_length=16, verbose_name="Номер телефона")
    work_position = models.CharField(blank=False, max_length=128, verbose_name="Должность")
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="ID компании")

    def __str__(self):  # название документа
        return self.full_name

    class Meta:
        verbose_name = "Сотрудник"  # человеческое название модели


class DocumentContract(models.Model):
    """Модель для документов договоров"""

    class ContractType(models.TextChoices):
        """Возможные значения вида договора"""
        WITH_CUSTOMER = "С заказчиком", "С заказчиком"
        WITH_COUNTERPARTY = "С контрагентом", "С контрагентом"

    class Currency(models.TextChoices):
        """Возможные значения валюты"""
        RUB = "Руб", "Руб"
        USD = "Дол", "Дол"
        EURO = "Евро", "Евро"

    class Status(models.TextChoices):
        """Возможные значения статуса договора"""
        FOR_SIGNING = "На подписании", "На подписании"
        SIGNED_ORIGINAL = "Подписан(оригинал)", "Подписан(оригинал)"
        SIGNED_COPY = "Подписан(копия)", "Подписан(копия)"

    date = models.DateField(verbose_name="Дата договора")  # дата договора
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создавший пользователь")
    number = models.CharField(max_length=256, unique=True, verbose_name="Номер договора")  # номер
    customer = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                 verbose_name="Заказчик", related_name='customer')  # заказчик - будет внешний ключ
    contractor = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                   verbose_name="Исполнитель",
                                   related_name='contractor')  # исполнитель - будет внешний ключ
    contract_type = models.CharField(max_length=256, choices=ContractType.choices,
                                     verbose_name="Вид договора")  # вид договора
    currency = models.CharField(max_length=32, choices=Currency.choices, verbose_name="Валюта")  # валюта
    status = models.CharField(max_length=64, choices=Status.choices, verbose_name="Статус")  # статус
    status_date = models.DateField(verbose_name="Дата статуса")  # дата статуса
    sbt = models.BooleanField(default=False, verbose_name="Принят по Sbt")  # принят по sbt
    contract_start_date = models.DateField(verbose_name="Дата начала договора")  # дата начала договора
    contract_stop_date = models.DateField(verbose_name="Дата конца договора")  # дата конца договора
    tracking = models.CharField(max_length=32, verbose_name="Отслеживание", blank=True)  # отслеживание
    printed_application_form = models.CharField(max_length=64,
                                                verbose_name="Печатная форма заявки",
                                                blank=True)  # печатная форма заявки
    counterparty_agreement_form = models.BooleanField(default=False,
                                                      verbose_name="Форма договора контрагента")  # Форма договора контрагента
    counterparty_application_form = models.BooleanField(default=False,
                                                        verbose_name="Форма заявок контрагента")  # Форма заявок контрагента
    additional_agreement = models.BooleanField(default=False,
                                               verbose_name="Есть дополнительное соглашение")  # есть доп соглашение
    rates_set_by_contract = models.BooleanField(default=False, verbose_name="Ставки установлены договором")
    contract_scan = models.FileField(upload_to="contract_scan/%Y%m/", blank=True, verbose_name="Скан договора")
    # скан договора
    note = models.TextField(verbose_name="Примечание", blank=True)  # примечание к документу

    def __str__(self):  # название документа
        return f"Документ {self.contract_type} номер {self.number} от {self.date}"

    class Meta:
        verbose_name = "Документ договора"  # человеческое название модели
        ordering = ["date"]  # сортировка