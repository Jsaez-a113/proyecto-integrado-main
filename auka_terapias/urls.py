"""
URL configuration for auka_terapias project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views as products_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
]

# Handlers para páginas de error personalizadas
handler404 = products_views.custom_404
handler500 = products_views.custom_500
handler403 = products_views.custom_403
handler400 = products_views.custom_400

# Servir archivos media y static SIEMPRE (incluso con DEBUG=False)
# En producción real, usa nginx/apache en su lugar
from django.views.static import serve
from django.urls import re_path

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

# Catch-all al final para capturar URLs no encontradas
# NOTA: Comentado porque interfiere con el servicio de archivos media
# Si necesitas páginas 404 personalizadas, usa handler404 arriba
# urlpatterns.append(path('<path:path>', products_views.custom_404))

