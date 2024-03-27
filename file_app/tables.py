"""Файл для определения таблиц (для динамического представления)"""

import django_tables2 as tables
from django_tables2.utils import A

from .models import DocumentContract, Company, Employee


class DocumentContractTable(tables.Table):
    """класс таблицы для документов договоров"""
    edit = tables.LinkColumn(
        "document-update",
        verbose_name="",
        text="Изменить",
        args=[A("pk")],
        orderable=False,
    )
    history = tables.LinkColumn(
        "document-history", 
        verbose_name="",
        text="🕵️", 
        args=[A("pk")], 
        orderable=False)


    class Meta:
        model = DocumentContract
        order_by = "number"  # сортировка по номеру
        template_name = "django_tables2/bootstrap.html"
        exclude = (
            "id",
            "user",
            "counterparty_agreement_form",
            "counterparty_application_form",
            "additional_agreement",
            "rates_set_by_contract",
            "contract_scan",
        )  # какие столбцы не показывать
        sequence = (
            "number",
            "date",
            "contract_type",
            "...",
            "sbt",
            "status",
            "note",
            "edit",
            # "history"
        )  # изменение порядка столбцов


class CompanyTable(tables.Table):
    """Класс таблицы для компаний"""
    detail = tables.LinkColumn("detail_company", verbose_name="Детали", text="Детали", args=[A("pk")], orderable=False)

    class Meta:
        model = Company
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id", "is_counterparty", "is_contractor")


class EmployeeTable(tables.Table):
    """Класс таблицы для сотрудников"""

    class Meta:
        model = Employee
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id",)
