from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    last_name = forms.CharField(max_length=30, required=True, label='Apellido')
    phone = forms.CharField(
        max_length=15,
        required=True,
        label='Teléfono',
        help_text='Formato: +56912345678, 56912345678 o 912345678',
    )
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Limpiar el número (quitar espacios, guiones, etc.)
            phone_clean = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
            # Validar formato chileno: debe empezar con +56, 56 o 9 y tener 9 dígitos después del 9
            import re
            if not re.match(r'^(\+?56)?9\d{8}$', phone_clean):
                raise forms.ValidationError('Ingrese un número de teléfono chileno válido (ej: +56912345678, 56912345678 o 912345678)')
            return phone_clean
        return phone
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            # Crear o actualizar el perfil con el teléfono
            from .models import UserProfile
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.phone = self.cleaned_data['phone']
            profile.save()
        return user

