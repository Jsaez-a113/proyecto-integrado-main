from django.contrib import admin
from .models import CartItem, Order, OrderItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'created']
    list_filter = ['created']
    search_fields = ['user__username', 'product__nombre']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['product_name', 'product_price', 'quantity', 'get_total']
    extra = 0
    
    def get_total(self, obj):
        return obj.get_total()
    get_total.short_description = 'Total'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total', 'status', 'created']
    list_filter = ['status', 'created']
    search_fields = ['user__username', 'id']
    readonly_fields = ['created', 'updated']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_name', 'product_price', 'quantity', 'get_total']
    list_filter = ['order__created']
    search_fields = ['product_name', 'order__id']
    
    def get_total(self, obj):
        return obj.get_total()
    get_total.short_description = 'Total'

