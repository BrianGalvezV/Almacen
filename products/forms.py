from django import forms
from django.contrib.auth.forms import User
from .models import Products

class ProductsForm(forms.ModelForm):

    class Meta:
        model= Products
        fields= ('name', 'description', 'quantity', 'price' )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.TextInput(attrs={'class': 'form-control'}),
            'quantity' : forms.NumberInput(attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control'}),

        }
