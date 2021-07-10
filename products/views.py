from django.shortcuts import render

#Forms
from .forms import ProductsForm

# Create your views here.
def products_list(request):
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