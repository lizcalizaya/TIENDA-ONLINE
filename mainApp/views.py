# Vista principal del catálogo de productos - comentario aclaratorio

from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import Producto

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {
        'productos': productos
    })



def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'producto_detalle.html', {
        'producto': producto
    })