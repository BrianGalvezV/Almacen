"""almacen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from products.views import products, products_list, delete_item, edit_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product', products, name="agregar_producto"),
    path('list', products_list, name="lista_productos"),
    path('edit/<id>', edit_item, name="editar_producto"),
    path('delete_item/<id>/', delete_item, name="eliminar_producto" ),
    path('', LoginView.as_view(template_name='login.html'), name="login"),
]
