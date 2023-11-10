from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class create_Rol(forms.Form):
    rol_nombre = forms.CharField(label = 'Nombre', max_length = 50)
    rol_descripcion = forms.CharField(label = 'Descripción', max_length = 100)


class create_User(forms.Form):
    usuario_nickname = forms.CharField(label = 'Nombre', max_length = 20)
    usuario_correo = forms.EmailField(label = 'Correo', max_length = 40)
    usuario_password = forms.CharField(label = 'Contraseña', max_length = 20, widget = forms.PasswordInput)
    """roles = (
        ('Vendedor', 'Vendedor'),
        ('Mecanico', 'Mecanico'),
        ('3', '3'),
        widget=forms.RadioSelect
    )"""
    usuario_rol = forms.ChoiceField(label = 'Rol')

#formulario personalizado con la tabla user
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True, help_text='Ingrese una Dirección de Correo Valida')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)



