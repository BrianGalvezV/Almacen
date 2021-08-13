from django import forms
from django.contrib.auth.forms import AuthenticationForm
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

class UserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
        
    }), label="Usuario")

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password"
        
    }), label="Contraseña")