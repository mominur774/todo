from django import forms
from django.forms import widgets
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['item']

        labels = {
            'item': ''
        }

        widgets = {
            'item': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }
