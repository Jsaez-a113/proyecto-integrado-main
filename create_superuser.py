"""
Script para crear superusuario automáticamente en Railway
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auka_terapias.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Obtener credenciales desde variables de entorno
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superusuario "{username}" creado exitosamente!')
else:
    if User.objects.filter(username=username).exists():
        print(f'El superusuario "{username}" ya existe.')
    else:
        print('No se configuró DJANGO_SUPERUSER_PASSWORD. Superusuario no creado.')
