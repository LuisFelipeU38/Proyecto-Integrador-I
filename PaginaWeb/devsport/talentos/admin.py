from django.contrib import admin
from .models import CustomUser
from .models import Jugador 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'user_type', 'is_staff')
    list_filter = ('user_type',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('nombre', 'apellidos', 'email', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'nombre', 'apellidos', 'email', 'password1', 'password2', 'user_type'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombre', 'apellidos', 'categoria')
    list_filter = ('categoria','posicion')
    search_fields = ('username', 'nombre', 'apellidos')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('nombre', 'apellidos', 'email')}),
        ('Información de Jugador', {'fields': ('categoria', 'peso', 'estatura', 'fecha_nacimiento', 'posicion')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'nombre', 'apellidos', 'password1', 'password2', 'categoria', 'peso', 'estatura', 'fecha_nacimiento', 'posicion'),
        }),
    )



# Register your models here.
