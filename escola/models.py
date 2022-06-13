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


# Create your models here.
