from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Docente  # Importar Usuario y los modelos creados


# 1. Registras el modelo Usuario utilizando UserAdmin
@admin.register(Usuario)
class UsuarioPersonalizadoAdmin(UserAdmin):
    pass

# 2. Registras los demás modelos creados (Persona NO se registra si es abstracta)
@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'fecha_nacimiento', 'legajo', 'especialidad')

    