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

'''
def create_document_contract(request):
    if request.method == "POST":
        form = DocumentContractForm(request.POST or None)
        print(form)
        if form.is_valid():
            doc = form.save()
            context = {"document": doc}
            return render(request, "file_app/create_document_contract.html", context)
    return render(request, "file_app/create_document_contract.html", {"form": DocumentContractForm()})

'''


class DocumentCreate(LoginRequiredMixin, CreateView):
    model = DocumentContract
    template_name = "file_app/create_document_contract.html"
    fields = '__all__'
    success_url = reverse_lazy("document_table")


class DocumentUpdate(LoginRequiredMixin, UpdateView):
    template_name = "file_app/edit_document_contract.html"
    model = DocumentContract
    fields = '__all__'
    success_url = reverse_lazy("document_table")


'''
    def form_valid(self, form):
        #form.instance.user = self.request.user
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
