from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Pedido, PedidoImagenes
from django.utils import timezone
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
    return render(request, 'producto_detalle.html', {'producto': producto})



def crear_pedido(request, producto_id=None):
    producto = None

    if producto_id:
        producto = get_object_or_404(Producto, id=producto_id)

    if request.method == "POST":
        form = PedidoForm(request.POST, request.FILES)

        if form.is_valid():
            pedido = form.save(commit=False)

            if producto:
                pedido.producto = producto

            pedido.plataforma = 'web'
            pedido.estado = 'solicitado'
            pedido.pago = 'pendiente'
            pedido.fecha_creado = timezone.now()
            pedido.save()

            
            for img in request.FILES.getlist('imagenes'):
                PedidoImagenes.objects.create(pedido=pedido, imagen=img)

            return redirect('pedido_confirmado', token=pedido.token)

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

    return render(request, 'seguimiento.html', {'pedido': pedido})



def pedido_confirmado(request, token):
    return render(request, 'pedido_confirmado.html', {'token': token})

def seguir_seguimiento(request):
    token = request.GET.get("codigo")

    if token:
        return redirect("seguimiento", token=token)

    return render(request, "seguir_seguimiento.html")
