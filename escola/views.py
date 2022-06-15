from rest_framework import viewsets 
from .models import Aluno, Curso
from .serializer import AlunoSerializer, CursoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
	"""Exibe todos os Alunos"""
	queryset = Aluno.objects.all()
	serializer_class = AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
	"""Exibe todos os Cursos"""
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer



# Create your views here.
