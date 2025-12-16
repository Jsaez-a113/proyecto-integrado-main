from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    CATEGORIA_CHOICES = [
        ('medicinal', 'Medicinal'),
        ('cosmetico', 'Cosmético'),
    ]
    
    nombre = models.CharField(max_length=200)
    beneficios = models.TextField()
    description = models.TextField()
    categorizacion = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='productos/', blank=True, null=True)
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    destacado = models.BooleanField(default=False, help_text="Marcar para mostrar en productos destacados")
    oculto = models.BooleanField(default=False, help_text="Marcar para ocultar el producto del catálogo")
    sin_stock = models.BooleanField(default=False, help_text="Marcar si el producto está sin stock")
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'
    
    def __str__(self):
        return f"{self.user.username} - {self.product.nombre} - {self.rating} estrellas"


class ContenidoQuienesSomos(models.Model):
    """Modelo para almacenar el contenido editable de la página Quienes Somos"""
    titulo = models.CharField(max_length=200, default="Quienes Somos")
    titulo_icono = models.CharField(
        max_length=100,
        default='fas fa-leaf',
        help_text="Clase de Font Awesome para el icono del título principal",
    )
    titulo_icono_color = models.CharField(
        max_length=7,
        default='#198754',
        help_text="Color hexadecimal del icono del título principal",
    )
    imagen_url = models.URLField(blank=True, null=True, help_text="URL de la imagen principal")
    imagen_archivo = models.ImageField(upload_to='contenido/', blank=True, null=True, help_text="O subir una imagen desde el ordenador")
    historia_titulo = models.CharField(max_length=200, default="Nuestra Historia")
    historia_icono = models.CharField(
        max_length=100,
        default='fas fa-seedling',
        help_text="Icono para la sección Nuestra Historia",
    )
    historia_icono_color = models.CharField(
        max_length=7,
        default='#0d6efd',
        help_text="Color del icono para la sección Nuestra Historia",
    )
    historia_texto = models.TextField()
    mision_titulo = models.CharField(max_length=200, default="Nuestra Misión")
    mision_icono = models.CharField(
        max_length=100,
        default='fas fa-heart',
        help_text="Icono para la sección Nuestra Misión",
    )
    mision_icono_color = models.CharField(
        max_length=7,
        default='#dc3545',
        help_text="Color del icono para la sección Nuestra Misión",
    )
    mision_texto = models.TextField()
    valores_titulo = models.CharField(max_length=200, default="Nuestros Valores")
    valores_icono = models.CharField(
        max_length=100,
        default='fas fa-certificate',
        help_text="Icono para la sección Nuestros Valores",
    )
    valores_icono_color = models.CharField(
        max_length=7,
        default='#0d6efd',
        help_text="Color del icono para la sección Nuestros Valores",
    )
    valores = models.JSONField(default=list, blank=True, help_text="Lista de valores en formato JSON")
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Contenido Quienes Somos'
        verbose_name_plural = 'Contenido Quienes Somos'
    
    def __str__(self):
        return "Contenido Quienes Somos"
    
    def save(self, *args, **kwargs):
        # Solo permitir una instancia
        self.pk = 1
        
        # Si ya existe una instancia, eliminar la imagen anterior
        try:
            old_instance = ContenidoQuienesSomos.objects.get(pk=1)
            # Si hay una nueva imagen y es diferente a la anterior, eliminar la anterior
            if old_instance.imagen_archivo and self.imagen_archivo and old_instance.imagen_archivo != self.imagen_archivo:
                # Eliminar el archivo físico del sistema
                if old_instance.imagen_archivo.name:
                    old_instance.imagen_archivo.delete(save=False)
        except ContenidoQuienesSomos.DoesNotExist:
            pass
        
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class ContenidoServiciosTerapeuticos(models.Model):
    """Modelo para almacenar el contenido editable de la página Servicios Terapéuticos"""
    titulo = models.CharField(max_length=200, default="Servicios Terapéuticos")
    subtitulo = models.CharField(max_length=300, default="Masajes y terapias naturales para tu bienestar integral")
    mensaje_agenda_titulo = models.CharField(max_length=200, default="Agenda Tu Sesión")
    mensaje_agenda_texto = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Contenido Servicios Terapéuticos'
        verbose_name_plural = 'Contenido Servicios Terapéuticos'
    
    def __str__(self):
        return "Contenido Servicios Terapéuticos"
    
    def save(self, *args, **kwargs):
        # Solo permitir una instancia
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class ServicioTerapeutico(models.Model):
    """Modelo para almacenar cada servicio terapéutico individual"""
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    icono = models.CharField(max_length=100, default='fas fa-spa', help_text="Clase de Font Awesome (ej: fas fa-hands)")
    color_icono = models.CharField(max_length=7, default='#667eea', help_text="Color del icono en formato hexadecimal (ej: #667eea)")
    items = models.JSONField(default=list, blank=True, help_text="Lista de características del servicio (ej: ['Duración: 60 minutos', 'Reduce el estrés'])")
    orden = models.IntegerField(default=0, help_text="Orden de visualización (menor número aparece primero)")
    activo = models.BooleanField(default=True, help_text="Marcar para mostrar el servicio en la página")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Servicio Terapéutico'
        verbose_name_plural = 'Servicios Terapéuticos'
        ordering = ['orden', 'created']
    
    def __str__(self):
        return self.titulo


class FotoBienvenida(models.Model):
    """Modelo para almacenar la foto de bienvenida del home"""
    titulo = models.CharField(max_length=200, default="Bienvenido a Auka Terapias")
    texto = models.TextField(default="Productos naturales para tu bienestar")
    imagen_url = models.URLField(blank=True, null=True, help_text="URL de la imagen")
    imagen_archivo = models.ImageField(upload_to='bienvenida/', blank=True, null=True, help_text="O subir una imagen desde el ordenador")
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Foto de Bienvenida'
        verbose_name_plural = 'Foto de Bienvenida'
    
    def __str__(self):
        return "Foto de Bienvenida"
    
    def save(self, *args, **kwargs):
        # Solo permitir una instancia
        self.pk = 1
        
        # Si ya existe una instancia, eliminar la imagen anterior
        try:
            old_instance = FotoBienvenida.objects.get(pk=1)
            # Si hay una nueva imagen y es diferente a la anterior, eliminar la anterior
            if old_instance.imagen_archivo and self.imagen_archivo and old_instance.imagen_archivo != self.imagen_archivo:
                # Eliminar el archivo físico del sistema
                if old_instance.imagen_archivo.name:
                    old_instance.imagen_archivo.delete(save=False)
        except FotoBienvenida.DoesNotExist:
            pass
        
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class ConfiguracionSitio(models.Model):
    """Modelo para almacenar las configuraciones generales del sitio"""
    nombre_navbar = models.CharField(
        max_length=100,
        default="AUKA",
        blank=True,
        null=True,
        help_text="Nombre que aparece en la barra superior (navbar) junto al icono"
    )
    nombre_navegador = models.CharField(
        max_length=200, 
        default="Auka Terapias - Productos Naturales",
        help_text="Título que aparece en la pestaña del navegador"
    )
    favicon = models.ImageField(
        upload_to='configuracion/', 
        blank=True, 
        null=True, 
        help_text="Icono que aparece junto al nombre en la barra superior (navbar) (recomendado: 32x32 píxeles)"
    )
    texto_footer = models.TextField(
        default="Auka Terapias - Productos medicinales y cosméticos 100% naturales, cultivados con amor y dedicación para cuidar tu bienestar.",
        help_text="Texto que aparece en el footer del sitio"
    )
    url_instagram = models.URLField(
        blank=True, 
        null=True, 
        default="https://www.instagram.com/auka_terapias/?hl=es",
        help_text="URL de Instagram para el footer"
    )
    url_whatsapp_footer = models.URLField(
        blank=True, 
        null=True, 
        default="https://wa.me/56985661992",
        help_text="URL de WhatsApp para el footer (formato: https://wa.me/56985661992)"
    )
    numero_pedidos = models.CharField(
        max_length=20,
        default="+56985661992",
        help_text="Número de WhatsApp para recibir pedidos (formato: +56985661992)"
    )
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Configuración del Sitio'
        verbose_name_plural = 'Configuración del Sitio'
    
    def __str__(self):
        return "Configuración del Sitio"
    
    def save(self, *args, **kwargs):
        # Solo permitir una instancia
        self.pk = 1
        
        # Si ya existe una instancia, eliminar el favicon anterior
        try:
            old_instance = ConfiguracionSitio.objects.get(pk=1)
            # Si hay un nuevo favicon y es diferente al anterior, eliminar el anterior
            if old_instance.favicon and self.favicon and old_instance.favicon != self.favicon:
                # Eliminar el archivo físico del sistema
                if old_instance.favicon.name:
                    old_instance.favicon.delete(save=False)
        except ConfiguracionSitio.DoesNotExist:
            pass
        
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

