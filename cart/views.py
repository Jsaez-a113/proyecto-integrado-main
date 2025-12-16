from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import CartItem, Order, OrderItem
from products.models import Product, ConfiguracionSitio


@login_required
def add_to_cart(request, product_id):
    """Añade un producto al carrito"""
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f'{product.nombre} añadido al carrito')
    return redirect('cart_view')


@login_required
def remove_from_cart(request, item_id):
    """Remueve un item del carrito"""
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, 'Producto removido del carrito')
    return redirect('cart_view')


@login_required
def update_cart(request, item_id):
    """Actualiza la cantidad de un item en el carrito"""
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, 'Carrito actualizado')
    else:
        cart_item.delete()
        messages.success(request, 'Producto removido del carrito')
    
    return redirect('cart_view')


@login_required
def cart_view(request):
    """Muestra el carrito de compras"""
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total() for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'cart/cart.html', context)


@login_required
def send_whatsapp(request):
    """Envía el mensaje de WhatsApp con los productos del carrito"""
    cart_items = CartItem.objects.filter(user=request.user)
    
    if not cart_items.exists():
        messages.error(request, 'Tu carrito está vacío')
        return redirect('cart_view')
    
    # Crear orden
    total = sum(item.get_total() for item in cart_items)
    order = Order.objects.create(user=request.user, total=total, status='pending')
    
    # Crear items de la orden y reducir stock
    productos_lista = []
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product_name=item.product.nombre,
            product_price=item.product.precio,
            quantity=item.quantity
        )
        # Reducir stock del producto
        item.product.stock -= item.quantity
        if item.product.stock < 0:
            item.product.stock = 0
        item.product.save()
        productos_lista.append(f"{item.product.nombre} (x{item.quantity})")
    
    # Obtener número de WhatsApp desde la configuración del sitio
    configuracion = ConfiguracionSitio.load()
    numero_whatsapp = configuracion.numero_pedidos.replace('+', '').replace(' ', '').replace('-', '')
    
    # Mensaje de WhatsApp
    mensaje = "hola, quiero concretar la compra de estos productos: " + ", ".join(productos_lista)
    mensaje_encoded = mensaje.replace(" ", "%20").replace(",", "%2C")
    
    whatsapp_url = f"https://wa.me/{numero_whatsapp}?text={mensaje_encoded}"
    
    # Limpiar carrito
    cart_items.delete()
    
    messages.success(request, 'Redirigiendo a WhatsApp para concretar tu compra...')
    return redirect(whatsapp_url)

