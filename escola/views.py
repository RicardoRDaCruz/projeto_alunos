from rest_framework import viewsets 
from .models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
	"""Exibe todos os Alunos"""
	queryset = Aluno.objects.all()
	serializer_class = AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
	"""Exibe todos os Cursos"""
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
	"""Exibe todos os Cursos"""
	queryset = Matricula.objects.all()
	serializer_class = MatriculaSerializer


# Create your views here.
