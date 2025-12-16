from .models import CartItem


def cart(request):
    """Context processor para mostrar el conteo del carrito en todas las páginas"""
    try:
        if request.user.is_authenticated:
            cart_count = CartItem.objects.filter(user=request.user).count()
        else:
            cart_count = 0
    except (AttributeError, TypeError):
        # Manejar caso donde request.user no está disponible
        cart_count = 0
    return {'cart_count': cart_count}

