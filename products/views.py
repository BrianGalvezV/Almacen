from django.shortcuts import render, redirect, get_object_or_404

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
            data['mensaje']= 'Elemento Guardado'

        else:
            data['form'] = formulario
            
    return render(request, 'products.html', data)

def products_list(request):
    productos = Products.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'lista.html', data)

def edit_item(request, id):
    producto = get_object_or_404(Products, id=id)
    data= {
        'form': ProductsForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductsForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="lista_productos")

        else:
            data['form'] = formulario

    return render(request, 'modificar.html', data)

def delete_item(request, id):
    producto = get_object_or_404(Products, id=id)
    producto.delete()

    return redirect(to="lista_productos")
