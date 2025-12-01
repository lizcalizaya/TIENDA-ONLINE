

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.catalogo, name='catalogo'),
    path('pedido/', views.crear_pedido, name='pedido_crear'),
    path('producto/<int:id>/', views.producto_detalle, name='producto_detalle'),
    path('seguimiento/<uuid:token>/', views.seguimiento, name='seguimiento'),
    path('pedido/<int:producto_id>/', views.crear_pedido, name='pedido_producto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
