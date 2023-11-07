from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm

def home(request):
    # Tu lógica de vista aquí
    return render(request, 'home.html')

def about(request):
    # Tu lógica de vista aquí
    return render(request, 'about.html')

def register_request(request):
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
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.user_type == 'jugador':
                    return redirect("vista_jugador")
                elif user.user_type == 'entrenador':
                    return redirect("vista_entrenador")
                elif user.user_type == 'admin':
                    return redirect("vista_admin")
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})

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
