from django.shortcuts import render, get_object_or_404
from .models import Curso, Profesor, Estudiante

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'core/estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'core/estudiante_detail.html', {'estudiante': estudiante})

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'core/profesores_list.html', {'profesores': profesores})

def detalle_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    return render(request, 'core/profesor_detail.html', {'profesor': profesor})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'core/cursos_list.html', {'cursos': cursos})

def detalle_cursos(request, pk):
    curso = get_object_or_404(Profesor, pk=pk)
    return render(request, 'core/curso_detail.html', {'curso': curso})


def index(request):
    return render(request, 'core/index.html')

