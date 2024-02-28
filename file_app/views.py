import os
import uuid
from .models import JournalContract, JournalContractType
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, Http404
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView


class JournalOrdersView(LoginRequiredMixin, View):
    # template_name = "file_app/journals_and_orders.html"

    def get(self, request):
        return render(request, "file_app/journals_and_orders.html")


class JournalListView(LoginRequiredMixin, View):

    def get(self, request):
        # journal_type = 1
        journals = JournalContractType.objects.all()
        context = {'journals': journals}
        return render(request, "file_app/journal_list.html", context)


class JournalDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        journal_name = JournalContractType.objects.filter(id=pk)
        journal_rows = JournalContract.objects.filter(journal_type=journal_name[0])
        context = {'journal_rows': journal_rows, 'journal_name': journal_name[0], 'pk': pk}
        return render(request, "file_app/journal_detail.html", context)


class JournalTypeCreate(LoginRequiredMixin, CreateView):
    template_name = "file_app/journal_type_create.html"
    model = JournalContractType
    fields = ['name']
    success_url = reverse_lazy("journal-list")


class JournalRowCreate(LoginRequiredMixin, CreateView):
    template_name = "file_app/journal_row_create.html"
    model = JournalContract
    fields = "__all__"
    success_url = "/journal-detail/3"

    def form_valid(self, form):
        return super(JournalRowCreate, self).form_valid(form)
