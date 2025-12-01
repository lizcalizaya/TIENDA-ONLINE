                                                                Tienda Online – Proyecto Django

Proyecto académico desarrollado en Django que permite mostrar un catálogo de productos personalizados y gestionar pedidos enviados por los clientes desde un formulario web.

Funcionalidades principales:

* Catálogo público de productos con imágenes.

* Vista de detalle del producto.

* Filtro por categorías.

* Buscador de productos.

* Formulario para solicitar pedidos, con subida de imagen.

* Generación automática de un token único para seguimiento.

* Página para ver el estado del pedido usando el token.

* Panel de administración para gestionar:

            - Productos

            - Categorías

            - Pedidos

            -Inventario de insumos

_Funcionalidad Extra_

Modo oscuro (Dark Mode) con botón para activar/desactivar.

Guarda la preferencia del usuario con localStorage.



Instalación

Clonar el repositorio:

git clone https://github.com/lizcalizaya/TIENDA-ONLINE.git


Instalar dependencias:

pip install -r requirements.txt


Crear migraciones y aplicar:

python manage.py makemigrations
python manage.py migrate


Ejecutar servidor:

python manage.py runserver

 Usuario Administrador:
Usuario: admin
Contraseña: admin