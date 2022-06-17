from rest_framework import viewsets, generics
from .models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunoMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunoViewSet(viewsets.ModelViewSet):
	"""Exibe todos os Alunos"""
	queryset = Aluno.objects.all()
	serializer_class = AlunoSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


class CursoViewSet(viewsets.ModelViewSet):
	"""Exibe todos os Cursos"""
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class MatriculaViewSet(viewsets.ModelViewSet):
	"""Exibe todos os Cursos"""
	queryset = Matricula.objects.all()
	serializer_class = MatriculaSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
	"""Mostra todas as matrículas de um aluno específico"""
	def get_queryset(self):
		queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
		return queryset 
	serializer_class = ListaMatriculasAlunoSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
	"""Mostra todos os alunos matriculados em um curso específico"""
	def get_queryset(self):
		queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
		return queryset 
	serializer_class = ListaAlunoMatriculadosSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]
