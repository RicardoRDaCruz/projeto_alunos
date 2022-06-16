from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
	list_display = ('id','nome','rg','cpf','data_nascimento',)
	list_display_links = ('id','nome')
	search_fields = ('nome',)
	list_per_page = 20

admin.site.register(Aluno, AlunoAdmin)

class CursoAdmin(admin.ModelAdmin):
	list_display = ('id','codigo','descricao','nivel',)
	list_display_links = ('id','codigo')
	search_fields = ('codigo',)
	list_per_page = 20

admin.site.register(Curso, CursoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
	list_display = ('id','aluno','curso','periodo',)
	list_display_links = ('id',)
	list_per_page = 20

admin.site.register(Matricula, MatriculaAdmin)