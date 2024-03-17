from typing import Any, Dict

from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView, View
from django.contrib import messages

from .tables import DocumentContractTable, CompanyTable, EmployeeTable
from .models import DocumentContract, Company, Employee
from .forms import DocumentContractForm, CompanyForm, EmployeeForm, SBTDocumentUpdateForm

from django_tables2 import SingleTableView, MultiTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


def load_companies(request):
    """Для динамического заполнения выборов компаний в форме"""
    contract_type = request.GET.get("contract_type")
    print("Вид договора:", contract_type)
    is_counterparty = None
    is_contractor = None
    if contract_type == "С заказчиком":
        is_counterparty = False
        is_contractor = False
    elif contract_type == "С контрагентом":
        is_counterparty = True
        is_contractor = False
    companies = Company.objects.filter(is_counterparty=is_counterparty, is_contractor=is_contractor)
    context = {"companies": companies}
    return render(request, "file_app/company_options.html", context)


def load_employees(request):
    """Для динамического заполнения выборов сотрудников в форме"""
    print(request)
    company = request.GET.get("company")
    if not company:
        company = request.GET.get("contractor_company")
    print("Компания в load_employee:", company)
    employees = Employee.objects.filter(company_id=company)
    print("Employees в load_employee:", employees)
    context = {"employees": employees}
    return render(request, "file_app/employee_options.html", context)


class DocumentCreate(LoginRequiredMixin, CreateView):
    """Вью с формой создания документа"""
    form_class = DocumentContractForm
    template_name = "file_app/create_document_contract.html"

    success_url = reverse_lazy("document_table")

    def form_valid(self, form):  # валидация формы
        form.instance.user = self.request.user  # автоматическое присвоение создавшего юзера
        messages.success(self.request, "Документ успешно создан.")
        return super(DocumentCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.instance, sep="\n")
        return super(DocumentCreate, self).form_invalid(form)


class DocumentUpdate(LoginRequiredMixin, UpdateView):
    """Вью обновления (изменения) существующего документа"""

    template_name = "file_app/edit_document_contract.html"
    model = DocumentContract
    fields = (
        "date",
        "number",
        "customer",
        "contractor",
        "contract_type",
        "currency",
        "status",
        "status_date",
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

    def get_form_class(self):
        user = self.request.user
        if user.groups.filter(name='Сб').exists():
            return SBTDocumentUpdateForm
        return super().get_form_class()


class DocumentsMainView(LoginRequiredMixin, TemplateView):
    """Страница со ссылками на документы"""
    template_name = "file_app/documents.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user_groups = self.request.user.groups.values_list('name', flat=True)
        context["can_add_company_employee"] = 'Продажники' in user_groups
        return context


class CompanyDetailView(LoginRequiredMixin, View):
    """Страница деталей компании"""

    @staticmethod
    def get(request, pk):
        company = Company.objects.get(id=pk)
        employees = Employee.objects.filter(company_id=company.id)
        context = {"company": company, "employees": employees}
        return render(request, "file_app/company_detail.html", context)


class CompaniesView(LoginRequiredMixin, MultiTableMixin, TemplateView):
    """Страница с таблицами компаний"""
    template_name = "file_app/companies_list.html"
    tables = [
        CompanyTable(Company.objects.filter(is_counterparty=False, is_contractor=False)),
        CompanyTable(Company.objects.filter(is_counterparty=True, is_contractor=False)),
        CompanyTable(Company.objects.filter(is_counterparty=False, is_contractor=True)),
    ]

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tables'] = [
            CompanyTable(Company.objects.filter(is_counterparty=False, is_contractor=False)),
            CompanyTable(Company.objects.filter(is_counterparty=True, is_contractor=False)),
            CompanyTable(Company.objects.filter(is_counterparty=False, is_contractor=True)),
        ]
        return context


class CreateCompany(LoginRequiredMixin, View):
    """Страница создания компании или сотрудника"""

    @staticmethod
    def get(request, company_type):
        form = CompanyForm()
        context = {"company-type": company_type, "form": form}
        return render(request, "file_app/create_company_employee.html", context)

    @staticmethod
    def post(request, *args, **kwargs):
        company_form = CompanyForm(request.POST)
        kwargs["form"] = company_form
        if company_form.is_valid():
            if kwargs['company_type'] == "counterparty":
                company_form.instance.is_counterparty = True
            elif kwargs['company_type'] == "contractor":
                company_form.instance.is_contractor = True
            company_form.save()
            return HttpResponseRedirect(reverse("companies"))
        return render(request, "file_app/create_company_employee.html", kwargs)


class CreateEmployee(LoginRequiredMixin, View):
    """Страница создания компании или сотрудника"""

    def get(self, request, company_id):
        form = EmployeeForm
        context = {"company_id": company_id, "form": form}
        return render(request, "file_app/create_company_employee.html", context)

    @staticmethod
    def post(request, *args, **kwargs):
        employee_form = EmployeeForm(request.POST)
        kwargs["form"] = employee_form
        company_id = kwargs['company_id']
        if employee_form.is_valid():
            employee_form.instance.company_id = Company.objects.get(id=company_id)
            employee_form.save()
            next_url = request.POST.get("next", "/")
            print(next_url)

            return HttpResponseRedirect(reverse("detail_company", args=[company_id]))
        return render(request, "file_app/create_company_employee.html", kwargs)


class DocumentContractTableView(SingleTableView):
    """Страница с отображением таблицы"""

    model = DocumentContract
    table_class = DocumentContractTable
    template_name = "file_app/document_contract_table.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user_groups = self.request.user.groups.values_list('name', flat=True)
        context["form"] = DocumentContractForm
        context["can_add_document"] = 'Продажники' in user_groups
        return context
