# Vista principal del catálogo de productos - comentario aclaratorio

from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import Producto, Categoria, Pedido
from .forms import PedidoForm


def catalogo(request):

    categorias = Categoria.objects.all()

    
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()

   
    q = request.GET.get('q')
    if q:
        productos = productos.filter(nombre__icontains=q)

    return render(request, 'catalogo.html', {
        'productos': productos,
        'categorias': categorias
    })



def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'producto_detalle.html', {
        'producto': producto
    })

def crear_pedido(request, producto_id=None):
    producto = None
    if producto_id:
        producto = Producto.objects.get(id=producto_id)

    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.plataforma = "Página Web"
            pedido.producto = producto
            pedido.save()
            return render(request, 'pedido_confirmado.html', {'pedido': pedido})
    else:
        form = PedidoForm()

    return render(request, 'crear_pedido.html', {
        'form': form,
        'producto': producto
    })
def seguimiento(request, token):
    pedido = Pedido.objects.filter(token=token).first()

    if not pedido:
        return render(request, 'seguimiento_no_encontrado.html')

    return render(request, 'seguimiento.html', {
        'pedido': pedido
    })