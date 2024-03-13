from django import forms

from .models import DocumentContract # Company, Employee

#customer_companies = Company.objects.all()
#customer_companies = [(i.company_name, i.company_name) for i in customer_companies]


class DatePicker(forms.DateInput):
    input_type = 'date'


class DocumentContractForm(forms.ModelForm):
    #company = forms.ChoiceField(choices=customer_companies, label='Компания')  # поле выбора компаний
    field_order = ["date", "number", "contract_type", "company", ]

    class Meta:
        model = DocumentContract
        exclude = ["user", ]  # какие поля исключить
        widgets = {
            "date": DatePicker(),
            "status_date": DatePicker(),
            "contract_start_date": DatePicker(),
            "contract_stop_date": DatePicker(),
        }
