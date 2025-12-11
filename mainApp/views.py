from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Pedido, PedidoImagenes
from django.utils import timezone
from .forms import PedidoForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Count


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

@login_required
def reporte_pedidos(request):
    
    fecha_desde_str = request.GET.get('desde')
    fecha_hasta_str = request.GET.get('hasta')
    plataforma = request.GET.get('plataforma')

    
    pedidos = Pedido.objects.all()

   
    if fecha_desde_str:
        fecha_desde = datetime.strptime(fecha_desde_str, "%Y-%m-%d").date()
        pedidos = pedidos.filter(fecha_creado__date__gte=fecha_desde)

    if fecha_hasta_str:
        fecha_hasta = datetime.strptime(fecha_hasta_str, "%Y-%m-%d").date()
        pedidos = pedidos.filter(fecha_creado__date__lte=fecha_hasta)

    
    if plataforma and plataforma != 'todas':
        pedidos = pedidos.filter(plataforma=plataforma)

    
    resumen_por_estado = pedidos.values('estado').annotate(total=Count('id')).order_by('estado')

    
    etiquetas = [item['estado'] for item in resumen_por_estado]
    valores = [item['total'] for item in resumen_por_estado]

    context = {
        'resumen_por_estado': resumen_por_estado,
        'etiquetas': etiquetas,
        'valores': valores,
        'fecha_desde': fecha_desde_str or '',
        'fecha_hasta': fecha_hasta_str or '',
        'plataforma_seleccionada': plataforma or 'todas',
    }

    return render(request, 'reporte_pedidos.html', context)