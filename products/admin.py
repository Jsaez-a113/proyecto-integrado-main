from django.contrib import admin
from .models import Product, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categorizacion', 'precio', 'stock', 'destacado', 'created']
    list_filter = ['categorizacion', 'destacado', 'created']
    search_fields = ['nombre', 'description']
    readonly_fields = ['created', 'updated']
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'categorizacion', 'precio', 'stock', 'destacado')
        }),
        ('Descripción', {
            'fields': ('beneficios', 'description')
        }),
        ('Imagen', {
            'fields': ('img',)
        }),
        ('Fechas', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created']
    list_filter = ['rating', 'created']
    search_fields = ['product__nombre', 'user__username', 'comment']

