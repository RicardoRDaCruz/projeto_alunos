from django.db import models

class Aluno(models.Model):
	nome = models.CharField(max_length=100)
	rg = models.CharField(max_length=9)
	cpf = models.CharField(max_length=11)
	data_nascimento = models.DateField()

	def __str__(self):
		return self.nome

NIVEL = (
	('B', 'Básico'),
	('I', 'Intermediário'),
	('A', 'Avançado'),
)

class Curso(models.Model):
	codigo = models.CharField(max_length=10)
	descricao = models.TextField(max_length=100)
	nivel = models.CharField(max_length=1,choices=NIVEL, null=False, default='B')

	def __str__(self):
		return self.descricao

PERIODO = (
	('M', 'Matutino'),
	('V', 'Vespertino'),
	('N', 'Noturno'),
)

class Matricula(models.Model):
	aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
	periodo = models.CharField(max_length=1,choices=PERIODO, null=False, default='M')



# Create your models here.
