from django.contrib import admin

# Register your models here.
from apps.funcionarios.models import Funcionarios


@admin.register(Funcionarios)
class FuncionariosProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_sobrenome', 'email', 'data_criacao')
    search_fields = ('id', 'nome_sobrenome', 'email')
