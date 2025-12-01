from django.contrib import admin

from django.contrib import admin
from .models import Categoria, Producto, Insumo, Pedido, PedidoImagenes

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio_base', 'destacado')
    list_filter = ('categoria','destacado')
    search_fields = ('nombre', 'descripcion')

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'cantidad', 'unidad', 'marca', 'color')
    list_filter = ('tipo', 'marca', 'color')
    search_fields = ('nombre', 'tipo', 'marca', 'color')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_cliente', 'producto', 'plataforma', 'estado', 'pago', 'fecha_necesidad', 'fecha_creado')
    list_filter = ('plataforma', 'estado', 'pago')
    search_fields = ('nombre_cliente', 'email', 'telefono', 'descripcion')
    readonly_fields = ('token', 'fecha_creado')
       

@admin.register(PedidoImagenes)
class PedidoImagenesAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'imagen')

