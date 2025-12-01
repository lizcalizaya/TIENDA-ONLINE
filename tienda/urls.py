from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

  
    path('', views.catalogo, name='catalogo'),
    path('producto/<int:id>/', views.producto_detalle, name='producto_detalle'),
    path('pedido/<int:producto_id>/', views.crear_pedido, name='pedido_producto'),
    path('pedido/', views.crear_pedido, name='pedido_crear'),
    path('pedido/confirmado/<uuid:token>/', views.pedido_confirmado, name='pedido_confirmado'),
    path('seguimiento/<uuid:token>/', views.seguimiento, name='seguimiento'),
    path('seguir_seguimiento/', views.seguir_seguimiento, name='seguir_seguimiento'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


