"""Файл для определения таблиц (для динамического представления)"""
import django_tables2 as tables
from django_tables2.utils import A

from .models import DocumentContract


class DocumentContractTable(tables.Table):
    edit = tables.LinkColumn("document-update", text="Изменить", args=[A("pk")], orderable=False)

    class Meta:
        model = DocumentContract
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id", "user", "counterparty_agreement_form", "counterparty_application_form",
                   "additional_agreement", "rates_set_by_contract", "contract_scan",)  # какие столбцы не показывать
        # sequence = ()  # изменение порядка столбцов
