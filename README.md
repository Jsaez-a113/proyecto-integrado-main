# Auka Terapias - Sitio Web de E-commerce

Sitio web profesional para Auka Terapias, un emprendimiento de productos medicinales y cosméticos 100% naturales.

## 🚀 Características

- **4 Secciones principales:**
  - Home: Página de inicio con foto de temporada y productos destacados
  - Catálogo: Listado completo de productos con filtros y ordenamiento
  - Quienes Somos: Información sobre el emprendimiento
  - Servicios Terapéuticos: Información sobre masajes y terapias

- **Sistema de Usuarios:**
  - Registro e inicio de sesión
  - Perfil de usuario con historial de compras
  - Reseñas de productos

- **Carrito de Compras:**
  - Añadir productos al carrito
  - Envío por WhatsApp para concretar compra
  - Gestión de cantidades

- **Administración:**
  - Interfaz de Django Admin para gestionar productos
  - Sistema completo de pedidos y órdenes

## 📋 Requisitos

- Python 3.10 o superior
- Django 5.x
- SQLite (incluido con Python)

## 🔧 Instalación

### Paso 1: Crear entorno virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Paso 2: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Crear migraciones y aplicar

```bash
python manage.py makemigrations
python manage.py migrate
```

### Paso 4: Crear superusuario (admin)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear un usuario administrador.

### Paso 5: Ejecutar el servidor

```bash
python manage.py runserver
```

El sitio estará disponible en: `http://127.0.0.1:8000/`

El panel de administración estará en: `http://127.0.0.1:8000/admin/`

## 📁 Estructura del Proyecto

```
proyecto integrado/
├── auka_terapias/          # Configuración del proyecto
│   ├── settings.py        # Configuración principal
│   ├── urls.py            # URLs principales
│   └── ...
├── products/               # App de productos
│   ├── models.py          # Modelos Product y Review
│   ├── views.py           # Vistas de productos
│   ├── urls.py            # URLs de productos
│   └── admin.py           # Configuración del admin
├── accounts/               # App de usuarios
│   ├── models.py          # Modelo UserProfile
│   ├── views.py           # Vistas de autenticación
│   └── ...
├── cart/                   # App del carrito
│   ├── models.py          # Modelos CartItem, Order, OrderItem
│   ├── views.py           # Vistas del carrito
│   └── ...
├── templates/              # Templates HTML
│   ├── base.html          # Template base
│   ├── products/          # Templates de productos
│   ├── accounts/          # Templates de autenticación
│   └── cart/              # Templates del carrito
├── static/                 # Archivos estáticos (CSS, JS, imágenes)
├── manage.py              # Script de gestión de Django
└── requirements.txt       # Dependencias del proyecto
```

## 🎨 Tecnologías Utilizadas

- **Backend:** Django 5.x
- **Frontend:** Bootstrap 5 (CDN)
- **Iconos:** Font Awesome 6 (CDN)
- **Fuentes:** Google Fonts (Poppins)
- **Base de Datos:** SQLite

## 📝 Modelo de Producto

El modelo Product tiene los siguientes campos obligatorios:

- `nombre` (CharField): Nombre del producto
- `beneficios` (TextField): Beneficios del producto
- `description` (TextField): Descripción completa
- `categorizacion` (CharField): 'medicinal' o 'cosmetico'
- `precio` (DecimalField): Precio del producto
- `img` (URLField): URL de la imagen (imágenes remotas)
- `stock` (IntegerField): Cantidad disponible
- `created` (DateTimeField): Fecha de creación (automático)
- `updated` (DateTimeField): Fecha de actualización (automático)
- `destacado` (BooleanField): Para mostrar en productos destacados

## 🔐 Usando el Panel de Administración

1. Accede a `http://127.0.0.1:8000/admin/`
2. Inicia sesión con el superusuario creado
3. En la sección "Products" puedes:
   - Añadir nuevos productos
   - Editar productos existentes
   - Marcar productos como destacados
   - Ver y gestionar reseñas

4. En la sección "Cart" puedes:
   - Ver carritos de usuarios
   - Gestionar órdenes y cambiar su estado

## 📱 Funcionalidad de WhatsApp

Cuando un usuario completa su carrito y hace clic en "Enviar por WhatsApp":
- Se crea una orden en el sistema
- Se genera un mensaje con los productos seleccionados
- Se abre WhatsApp con el mensaje pre-escrito
- El número configurado es: +56 9 8566 1992

## 🎯 Redes Sociales

- Instagram: [@auka_terapias](https://www.instagram.com/auka_terapias/?hl=es)
- WhatsApp: +56 9 8566 1992

## 📄 Paginación

El catálogo muestra 10 productos por página con navegación completa.

## 🛠️ Personalización

### Cambiar número de WhatsApp

Edita `auka_terapias/settings.py`:
```python
WHATSAPP_NUMBER = '+56 9 8566 1992'  # Cambia este número
```

### Cambiar productos por página

Edita `products/views.py`, función `catalogo`:
```python
paginator = Paginator(productos, 10)  # Cambia el número 10
```

## 📝 Notas Importantes

- Las imágenes de productos deben ser URLs remotas (no archivos locales)
- El sitio usa SQLite por defecto (suficiente para desarrollo)
- Para producción, considera cambiar a PostgreSQL o MySQL
- Recuerda cambiar `SECRET_KEY` en `settings.py` para producción

## 🐛 Solución de Problemas

### Error: "No module named 'django'"
```bash
pip install -r requirements.txt
```

### Error: "No migrations to apply"
```bash
python manage.py makemigrations
python manage.py migrate
```

### Error: "Template not found"
Asegúrate de que la estructura de carpetas `templates/` esté correcta.

## 📞 Soporte

Para más información o ayuda, contacta a través de:
- WhatsApp: +56 9 8566 1992
- Instagram: @auka_terapias

---

**Desarrollado con ❤️ para Auka Terapias**

