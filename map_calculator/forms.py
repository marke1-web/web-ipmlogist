from django import forms


class DistanceForm(forms.Form):
    point_a = forms.CharField(label='Точка А')
    point_b = forms.CharField(label='Точка Б')
