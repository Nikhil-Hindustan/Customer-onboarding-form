# forms.py

from django import forms
from .models import CustomerModel, CustomerDocumentModel


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ['surname', 'first_name', 'nationality', 'gender']


class CustomerDocumentForm(forms.ModelForm):
    class Meta:
        model = CustomerDocumentModel
        fields = ['attached_file']
