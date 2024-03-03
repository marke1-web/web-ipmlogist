from typing import Any, Dict

from .tables import DocumentContractTable
from .models import DocumentContract
from .forms import DocumentContractForm

from django_tables2 import SingleTableView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class JournalOrdersView(LoginRequiredMixin, View):
    """Страница со ссылками на документы"""

    def get(self, request):
        return render(request, "file_app/documents.html")


class DocumentContractTableView(SingleTableView):
    """Страница с отображением таблицы"""
    model = DocumentContract
    table_class = DocumentContractTable
    template_name = "file_app/document_contract_table.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(DocumentContractTableView, self).get_context_data(**kwargs)
        context["form"] = DocumentContractForm
        return context
