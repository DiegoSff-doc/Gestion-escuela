from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Usuario del sistema para autenticación
class Usuario(AbstractUser):
    pass  # Hereda username, password, email, first_name, last_name, etc.

# 2. Clase Abstracta Padre (No crea tabla en la base de datos)
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True  # Indica a Django que solo se usará para herencia

# 3. Clase Hija de Ejemplo (Crea la tabla core_docente con su id automático)
class Docente(Persona):
    usuario = models.OneToOneField(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='perfil_docente'
    )
    legajo = models.CharField(max_length=20, unique=True)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"Prof. {self.apellido}, {self.nombre} ({self.legajo})"
