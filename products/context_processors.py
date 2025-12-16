from .models import ConfiguracionSitio


def configuracion_sitio(request):
    """Context processor para mostrar la configuración del sitio en todas las páginas"""
    try:
        configuracion = ConfiguracionSitio.load()
    except Exception:
        # Si hay algún error, crear una configuración por defecto
        configuracion = ConfiguracionSitio.load()
    
    return {
        'configuracion_sitio': configuracion,
    }

