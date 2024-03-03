from django import forms

from .models import DocumentContract


class DatePicker(forms.DateInput):
    input_type = 'date'


class DocumentContractForm(forms.ModelForm):
    class Meta:
        model = DocumentContract
        exclude = ["user", ]  # какие поля исключить
        widgets = {
            "date": DatePicker(),
            "status_date": DatePicker(),
            "contract_start_date": DatePicker(),
            "contract_stop_date": DatePicker(),
        }
