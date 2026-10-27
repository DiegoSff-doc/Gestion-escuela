from django.db import models
from ..core.models import Docente

class CicloLectivo(models.Model):
    anio  = models.PositiveSmallIntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField()
    
    def __str__(self) -> str:
        return f"Ciclo lectivo. {self.anio}, {self.fecha_inicio} ({self.fecha_fin}, {self.activo})"
    
class Curso(models.Model):
    ciclo_lectivo  = models.ForeignKey(        
        CicloLectivo, 
        on_delete=models.CASCADE, 
        related_name='Curso'
    )
    anio = models.PositiveSmallIntegerField()
    division = models.CharField(max_length=100)
    orientacion = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"Curso. {self.ciclo_lectivo}, {self.anio} ({self.division}, {self.orientacion})"
    
    def get_cantidad_alumnos(self) -> int:
        return self.estudiante.count()
        
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"Materia. {self.nombre}"
    
class Comision(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(        
        Curso, 
        on_delete=models.CASCADE, 
        related_name='Comision'
    )
    materia = models.ForeignKey(        
        Materia, 
        on_delete=models.CASCADE, 
        related_name='Comision'
    )
    docente = models.ForeignKey(        
        Docente, 
        on_delete=models.CASCADE, 
        related_name='Comision'
    )
    
    def __str__(self) -> str:
        return f"Comision. {self.nombre}, {self.curso}, {self.materia}, {self.docente}"
    
class Horario(models.Model):
    comision = models.ForeignKey(        
        Comision, 
        on_delete=models.CASCADE, 
        related_name='Horario'
    )
    dia = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    def __str__(self) -> str:
        return f"Horario. {self.comision}, {self.dia}, {self.fecha_inicio}, {self.fecha_fin}"
    
    # def get_dia_display() -> String:
    