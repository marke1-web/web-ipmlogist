from django import forms

from .models import DocumentContract


class DocumentContractForm(forms.ModelForm):
    class Meta:
        model = DocumentContract
        fields = "__all__"
