from rest_framework import serializers

from apps.empresas.serializers import GetEmpresasSerializer, PostEmpresaSerializer
from apps.funcionarios.models import Funcionarios


class PostFuncionariosSerializer(serializers.ModelSerializer):
    empresas = PostEmpresaSerializer(many=True)

    class Meta:
        model = Funcionarios
        fields = ('id', 'nome_sobrenome', 'email', 'empresas')


class GetFuncionariosSerializer(serializers.ModelSerializer):
    nome_sobrenome = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    data_criacao = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    empresas = GetEmpresasSerializer(many=True)

    class Meta:
        model = Funcionarios
        fields = ('id', 'nome_sobrenome', 'email', 'data_criacao', 'empresas')
