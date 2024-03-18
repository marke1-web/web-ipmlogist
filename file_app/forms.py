from django import forms

from .models import DocumentContract, Company, Employee


class SBTDocumentUpdateForm(forms.ModelForm):
    class Meta:
        model = DocumentContract
        fields = ("sbt",)


class DatePicker(forms.DateInput):
    """Виджет для выбора даты"""
    input_type = 'date'


class DocumentContractForm(forms.ModelForm):
    company = forms.ModelChoiceField(
        queryset=Company.objects.none(),
        label="Компания заказчик",
        widget=forms.Select(
            attrs={"hx-get": "./load_employees/", "hx-target": "#id_customer"})
    )  # поле компании

    contractor_company = forms.ModelChoiceField(
        queryset=Company.objects.filter(is_contractor=True),
        label="Компания исполнитель",
        widget=forms.Select(
            attrs={"hx-get": "./load_employees/", "hx-target": "#id_contractor"})
    )  # поле компании исполнителя

    contractor = forms.ModelChoiceField(
        queryset=Employee.objects.none(),
        label=" исполнитель"
    )  # поле исполнителя

    field_order = ["date", "number", "contract_type", "company", "customer", "contractor_company", ]  # порядок полей

    class Meta:
        model = DocumentContract
        exclude = ["user", "sbt"]  # какие поля исключить
        widgets = {
            "contract_type": forms.Select(attrs={"hx-get": "./load_companies/", "hx-target": "#id_company"}),
            "date": DatePicker(format='%Y-%m-%d'),
            "status_date": DatePicker(format='%Y-%m-%d'),
            "contract_start_date": DatePicker(format='%Y-%m-%d'),
            "contract_stop_date": DatePicker(format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "contractor" in self.data:
            contractor_id = self.data.get("contractor")
            print("contractor_id:", contractor_id)
            self.fields["contractor"].queryset = Employee.objects.filter(id=contractor_id)

        if "company" in self.data:
            company_id = self.data.get("company")
            print("company_id:", company_id)
            self.fields["company"].queryset = Company.objects.filter(id=company_id)

        """
        print("init:", self.initial)
        if "initial" in kwargs:
            if "company" in kwargs['initial']:
                print("initial in kwargs comapny in initial")
                self.initial['company'] = kwargs['initial']['company']
                print(self.initial['company'])
        """

class CompanyForm(forms.ModelForm):
    """Форма компании"""

    class Meta:
        model = Company
        fields = ['company_name', 'tax_identification_number']  # какие поля оставить


class EmployeeForm(forms.ModelForm):
    """Форма сотрудника"""

    class Meta:
        model = Employee
        exclude = ['company_id']  # какие поля исключить
