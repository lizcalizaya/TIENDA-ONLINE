from django.db import models

import uuid

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    imagen1 = models.ImageField(upload_to='productos/', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='productos/', blank=True, null=True)
    imagen3 = models.ImageField(upload_to='productos/', blank=True, null=True)

    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=20, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre

PLATAFORMAS = [
    ('facebook', 'Facebook'),
    ('instagram', 'Instagram'),
    ('whatsapp', 'WhatsApp'),
    ('presencial', 'Presencial'),
    ('web', 'Sitio Web'),
    ('otro', 'Otro'),
]

ESTADOS_PEDIDO = [
    ('solicitado', 'Solicitado'),
    ('aprobado', 'Aprobado'),
    ('proceso', 'En proceso'),
    ('realizada', 'Realizada'),
    ('entregada', 'Entregada'),
    ('finalizada', 'Finalizada'),
    ('cancelada', 'Cancelada'),
]

ESTADO_PAGO = [
    ('pendiente', 'Pendiente'),
    ('parcial', 'Parcial'),
    ('pagado', 'Pagado'),
]


class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)

    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)

    descripcion = models.TextField(blank=True, null=True)
    fecha_requerida = models.DateField(blank=True, null=True)

    plataforma = models.CharField(max_length=20, choices=PLATAFORMAS, default='web')
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default='solicitado')
    pago = models.CharField(max_length=20, choices=ESTADO_PAGO, default='pendiente')

    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente}"

class PedidoImagenes(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='referencias/')

    def __str__(self):
        return f"Imagen de {self.pedido}"



    





