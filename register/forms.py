from dataclasses import field
from tkinter import Widget
from django.core import validators
from django import forms
from .models import employee


class employeeRegistration(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['name', 'department']
        Widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }
