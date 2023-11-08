from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Jugador
from .forms import NewUserForm
from .forms import BusquedaJugadorForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

def home(request):
    # Tu lógica de vista aquí
    return render(request, 'home.html')

def about(request):
    # Tu lógica de vista aquí
    return render(request, 'about.html')

def register_request(request):
    if request.user.is_authenticated:
            return redirect('home')
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso.")
            return redirect("home")
        else:
            messages.error(request, "Registro no exitoso. Información no válida.")
    else:
        form = NewUserForm()
    return render(request, "register.html", {"register_form": form})

def login_request(request):
    if request.user.is_authenticated:
            return redirect('home')
    if request.method == "POST":
        # Procesa el formulario de inicio de sesión
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Inicia sesión al usuario
            if user.user_type == 'jugador':
                return redirect("vista_jugador")
            elif user.user_type == 'entrenador':
                return redirect("vista_entrenador")
            elif user.user_type == 'admin':
                return redirect("vista_admin")
        else:
            # Mostrar un mensaje de error si las credenciales son incorrectas
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "login.html")


@login_required
def vista_jugador(request):
    # Lógica para la vista de jugador
    return render(request, 'vista_jugador.html')

@login_required
def vista_entrenador(request):
    # Lógica para la vista de entrenador
    return render(request, 'vista_entrenador.html')

@login_required
def vista_admin(request):
    # Lógica para la vista de administrador
    return render(request, 'vista_admin.html') 

@login_required
def perfil(request):
    user = request.user  # Obtiene el usuario actual

    # Puedes pasar el usuario y otros datos que necesites al contexto
    context = {
        'user': user,
        # Agrega más datos según tus necesidades
    }

    return render(request, 'perfil.html', context)

def buscar_jugadores(request):
    jugadores = Jugador.objects.all()

    if request.method == 'GET':
        form = BusquedaJugadorForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            apellidos = form.cleaned_data.get('apellidos')
            categoria = form.cleaned_data.get('categoria')
            peso = form.cleaned_data.get('peso')
            estatura = form.cleaned_data.get('estatura')
            fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
            posicion = form.cleaned_data.get('posicion')

            if nombre:
                jugadores = jugadores.filter(nombre__icontains=nombre)

            if apellidos:
                jugadores = jugadores.filter(apellidos__icontains=apellidos)

            if categoria:
                jugadores = jugadores.filter(categoria=categoria)

            if peso:
                jugadores = jugadores.filter(peso=peso)

            if estatura:
                jugadores = jugadores.filter(estatura=estatura)

            if fecha_nacimiento:
                jugadores = jugadores.filter(fecha_nacimiento=fecha_nacimiento)

            if posicion:
                jugadores = jugadores.filter(posicion__icontains=posicion)

    else:
        form = BusquedaJugadorForm()

    return render(request, 'vista_entrenador.html', {'form': form, 'jugadores': jugadores})