from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def str(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

    def str(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100)
    estudiantes = models.CharField(max_length=100)
    numero_curso = models.IntegerField(max_length=100)
    fecha_inicio = models.DateField(max_length=15)
    fecha_fin = models.DateField(max_length=15)
    def str(self):
        return f"Nombre: {self.nombre} \n Profesor: {self.profesor} \n Comision: {self.numero_curso} \n  Fecha inicio: {self.fecha_inicio} \n Fecha fin: {self.fecha_fin}"
