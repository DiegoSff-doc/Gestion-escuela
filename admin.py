from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CicloLectivo, Curso, Materia, Comision, Horario  # Importar Usuario y los modelos creados


# 1. Registras el modelo Usuario utilizando UserAdmin
@admin.register(CicloLectivo)
class CicloLectivoAdmin(UserAdmin):
    list_display = ('anio', 'fecha_inicio', 'fecha_fin', 'activo')

@admin.register(Curso)  
class CursoAdmin(UserAdmin):
    list_display = ('ciclo_lectivo', 'anio', 'division', 'orientacion')
    
@admin.register(Materia)  
class MateriaAdmin(UserAdmin):
    list_display = ('nombre')
    
@admin.register(Comision)  
class ComisionAdmin(UserAdmin):
    list_display = ('nombre', 'curso', 'materia', 'docente')
    
@admin.register(Horario)
class HorarioAdmin(UserAdmin):
    list_display = ('comision', 'dia', 'fecha_inicio', 'fecha_fin', )
