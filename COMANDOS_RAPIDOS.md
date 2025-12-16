# ⚡ Comandos Rápidos

Guía rápida de comandos para trabajar con el proyecto.

## 🚀 Inicio Rápido

```bash
# 1. Activar entorno virtual
venv\Scripts\activate

# 2. Ejecutar servidor
python manage.py runserver
```

## 📦 Instalación Inicial

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

## 🔄 Comandos de Desarrollo

```bash
# Ejecutar servidor
python manage.py runserver

# Ejecutar en puerto específico
python manage.py runserver 8001

# Crear migraciones después de cambiar modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ver migraciones pendientes
python manage.py showmigrations
```

## 👤 Gestión de Usuarios

```bash
# Crear superusuario
python manage.py createsuperuser

# Cambiar contraseña de usuario
python manage.py changepassword <username>
```

## 🗄️ Base de Datos

```bash
# Ver migraciones aplicadas
python manage.py showmigrations

# Aplicar todas las migraciones
python manage.py migrate

# Revertir última migración
python manage.py migrate <app_name> <previous_migration>

# Crear migración vacía
python manage.py makemigrations --empty <app_name>
```

## 📊 Shell de Django

```bash
# Abrir shell de Django
python manage.py shell

# Ejemplo en shell:
# from products.models import Product
# Product.objects.all()
```

## 🧹 Limpieza

```bash
# Limpiar archivos .pyc
find . -type d -name __pycache__ -exec rm -r {} +
# O en Windows PowerShell:
Get-ChildItem -Path . -Recurse -Filter __pycache__ | Remove-Item -Recurse -Force

# Limpiar base de datos (CUIDADO: borra todo)
# Eliminar db.sqlite3 y ejecutar:
python manage.py migrate
```

## 📝 Crear Datos de Prueba

En el shell de Django (`python manage.py shell`):

```python
from products.models import Product

# Crear producto de ejemplo
Product.objects.create(
    nombre="Aceite de Lavanda",
    beneficios="Relajante, ayuda a dormir mejor, reduce el estrés",
    description="Aceite esencial 100% natural de lavanda cultivado orgánicamente. Ideal para masajes y aromaterapia.",
    categorizacion="medicinal",
    precio=15000,
    img="https://images.unsplash.com/photo-1615634260167-c8cdede054de?w=500",
    stock=50,
    destacado=True
)

# Crear producto cosmético
Product.objects.create(
    nombre="Crema Facial Natural",
    beneficios="Hidratante, anti-edad, suaviza la piel",
    description="Crema facial elaborada con ingredientes 100% naturales. Perfecta para todo tipo de piel.",
    categorizacion="cosmetico",
    precio=25000,
    img="https://images.unsplash.com/photo-1556229010-6c3f2c9ca5f8?w=500",
    stock=30,
    destacado=True
)
```

## 🐛 Debugging

```bash
# Ver configuración
python manage.py diffsettings

# Verificar proyecto
python manage.py check

# Verificar con más detalles
python manage.py check --deploy
```

## 📦 Dependencias

```bash
# Actualizar requirements.txt
pip freeze > requirements.txt

# Instalar nueva dependencia
pip install <paquete>
pip install <paquete>==<version>
```

## 🌐 Accesos Rápidos

- **Sitio:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/
- **Catálogo:** http://127.0.0.1:8000/catalogo/
- **Registro:** http://127.0.0.1:8000/accounts/register/
- **Login:** http://127.0.0.1:8000/accounts/login/

## ⚠️ Notas Importantes

- Siempre activa el entorno virtual antes de trabajar
- El servidor debe estar corriendo para ver los cambios
- Los cambios en templates se ven inmediatamente (recarga automática)
- Los cambios en modelos requieren `makemigrations` y `migrate`
- Usa `CTRL + C` para detener el servidor

