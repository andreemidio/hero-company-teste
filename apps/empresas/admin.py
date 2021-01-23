from django.contrib import admin

# Register your models here.
from apps.empresas.models import Empresas


@admin.register(Empresas)
class EmpresasProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'cnpj', 'razao_social', 'data_criacao')
    search_fields = ('id', 'cnpj', 'razao_social')
