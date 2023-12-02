# forms.py
from django import forms
from .models import Shifting
from datetime import datetime

class MyForm(forms.ModelForm):
    class Meta:
        model = Shifting
        fields = ['user', 'date', 'shift']
        widgets = {
            'date': forms.TextInput(attrs={'type': 'text'}),
        }
        input_formats = ['%Y-%m-%d']
        



'''widgets = {
            'date': forms.DateInput(format = "%Y-%m-%d",attrs={'type': 'text', 'placeholder': 'YYYY-MM-DD'}),
        }'''
    