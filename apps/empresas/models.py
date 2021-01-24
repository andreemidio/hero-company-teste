import uuid

from django.db import models
# Create your models here.
from sortedm2m.fields import SortedManyToManyField

from apps.funcionarios.models import Funcionarios


class Empresas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cnpj = models.CharField(max_length=14, db_index=True, unique=True)
    razao_social = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    funcionarios = SortedManyToManyField(Funcionarios)

    def __str__(self):
        return self.razao_social

    def __repr__(self):
        return self.razao_social

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['data_criacao']
