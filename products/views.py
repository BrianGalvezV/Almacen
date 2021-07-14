from django.shortcuts import render

#Models
from .models import Products

#Forms
from .forms import ProductsForm

# Create your views here.
def products(request):
    data = {
        'form': ProductsForm()
    }
    if request.method == 'POST':
        formulario = ProductsForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']= 'Mensaje Enviado'

        else:
            data['form'] = formulario
            
    return render(request, 'products.html', data)

def products_list(request):
    productos = Products.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'lista.html', data)