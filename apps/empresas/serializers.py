from rest_framework import serializers

from apps.empresas.models import Empresas
from apps.funcionarios.serializers import ListFuncionariosSerializer


class PostEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ('id', 'cnpj', 'razao_social')


class GetEmpresasSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    cnpj = serializers.CharField(required=True)
    razao_social = serializers.CharField(required=True)
    data_criacao = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    funcionarios = ListFuncionariosSerializer(many=True)

    class Meta:
        model = Empresas
        fields = ('id', 'cnpj', 'razao_social', 'data_criacao', 'funcionarios')



