from typing import Any, Dict

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .tables import DocumentContractTable
from .models import DocumentContract
from .forms import DocumentContractForm

from django_tables2 import SingleTableView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class DocumentCreate(LoginRequiredMixin, CreateView):
    """Вью с формой создания документа"""
    model = DocumentContract
    template_name = "file_app/create_document_contract.html"
    # fields = '__all__'
    fields = ("date",
              "number",
              "customer",
              "contractor",
              "contract_type",
              "currency",
              "status",
              "status_date",
              "sbt",
              "contract_start_date",
              "contract_stop_date",
              "tracking",
              "printed_application_form",
              "counterparty_agreement_form",
              "counterparty_application_form",
              "additional_agreement",
              "rates_set_by_contract",
              "contract_scan",
              "note",
              )
    success_url = reverse_lazy("document_table")

    def form_valid(self, form):  # валидация формы
        form.instance.user = self.request.user  # автоматическое присвоение создавшего юзера
        return super(DocumentCreate, self).form_valid(form)


class DocumentUpdate(LoginRequiredMixin, UpdateView):
    """Вью обновления (изменения) существующего документа"""
    template_name = "file_app/edit_document_contract.html"
    model = DocumentContract
    fields = ("date",
              "number",
              "customer",
              "contractor",
              "contract_type",
              "currency",
              "status",
              "status_date",
              "sbt",
              "contract_start_date",
              "contract_stop_date",
              "tracking",
              "printed_application_form",
              "counterparty_agreement_form",
              "counterparty_application_form",
              "additional_agreement",
              "rates_set_by_contract",
              "contract_scan",
              "note",
              )
    success_url = reverse_lazy("document_table")


'''
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DocumentCreate, self).form_valid(form)
'''


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
