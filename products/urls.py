from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/<int:product_id>/', views.product_detail, name='product_detail'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('servicios-terapeuticos/', views.servicios_terapeuticos, name='servicios_terapeuticos'),
    
    # URLs de administración
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/productos/', views.admin_productos, name='admin_productos'),
    path('admin-panel/productos/nuevo/', views.admin_producto_editar, name='admin_producto_nuevo'),
    path('admin-panel/productos/<int:product_id>/editar/', views.admin_producto_editar, name='admin_producto_editar'),
    path('admin-panel/productos/<int:product_id>/eliminar/', views.admin_producto_eliminar, name='admin_producto_eliminar'),
    path('admin-panel/contenido/quienes-somos/', views.admin_contenido_quienes_somos, name='admin_contenido_quienes_somos'),
    path('admin-panel/contenido/servicios/', views.admin_contenido_servicios, name='admin_contenido_servicios'),
    path('admin-panel/servicios/', views.admin_servicios_lista, name='admin_servicios_lista'),
    path('admin-panel/servicios/nuevo/', views.admin_servicio_editar, name='admin_servicio_nuevo'),
    path('admin-panel/servicios/<int:servicio_id>/editar/', views.admin_servicio_editar, name='admin_servicio_editar'),
    path('admin-panel/servicios/<int:servicio_id>/eliminar/', views.admin_servicio_eliminar, name='admin_servicio_eliminar'),
    path('admin-panel/foto-bienvenida/', views.admin_foto_bienvenida, name='admin_foto_bienvenida'),
    path('admin-panel/configuracion/', views.admin_configuracion, name='admin_configuracion'),
    path('admin-panel/pedidos/', views.admin_pedidos, name='admin_pedidos'),
    path('admin-panel/pedidos/<int:order_id>/actualizar/', views.admin_pedido_actualizar, name='admin_pedido_actualizar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)