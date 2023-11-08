from django import forms
from django.contrib.auth.forms import UserCreationForm
from talentos.models import Jugador
from django.forms.widgets import DateInput

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    CATEGORIAS = (
        ('Infantil', 'Infantil'),
        ('Juvenil', 'Juvenil'),
        ('Profesional', 'Profesional'),
    )
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    categoria = forms.ChoiceField(choices=CATEGORIAS)
    peso = forms.DecimalField(max_digits=5, decimal_places=2)
    estatura = forms.DecimalField(max_digits=4, decimal_places=2)
    fecha_nacimiento = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    posicion = forms.CharField(max_length=50)

    class Meta:
        model = Jugador
        fields = ('username', 'email', 'nombre', 'apellidos',  'fecha_nacimiento', 'categoria','posicion', 'peso', 'estatura', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'categoria': 'Categoría',
            'peso': 'Peso (kg)',
            'estatura': 'Estatura (m)',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'posicion': 'Posición',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class BusquedaJugadorForm(forms.Form):
    nombre = forms.CharField(required=False)
    apellidos = forms.CharField(required=False)
    categoria = forms.ChoiceField(choices=Jugador.CATEGORIAS, required=False)
    peso = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    estatura = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    fecha_nacimiento = forms.DateField(required=False)
    posicion = forms.CharField(required=False)