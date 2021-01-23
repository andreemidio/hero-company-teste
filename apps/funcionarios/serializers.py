from rest_framework import serializers

from apps.empresas.models import Empresas
from apps.funcionarios.models import Funcionarios


class PostFuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = ('id', 'nome_sobrenome', 'email')


class ListFuncionariosSerializer(serializers.ModelSerializer):
    nome_sobrenome = serializers.CharField(required=True)

    class Meta:
        model = Funcionarios
        fields = ('id', 'nome_sobrenome')


class GetFuncionariosSerializer(serializers.ModelSerializer):
    nome_sobrenome = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    data_criacao = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Funcionarios
        fields = ('id', 'nome_sobrenome', 'email', 'data_criacao')


class ListEmpresasSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField()
    cnpj = serializers.CharField(required=True)
    razao_social = serializers.CharField(required=True)
    data_criacao = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Empresas
        fields = ("id", "cnpj", "razao_social", "data_criacao")


class GetFuncionariosEmpresasSerializer(serializers.HyperlinkedModelSerializer):
    nome_sobrenome = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    data_criacao = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    empresas_set = ListEmpresasSerializer(many=True, read_only=True)

    class Meta:
        model = Funcionarios
        fields = ('id', 'nome_sobrenome', 'email', 'data_criacao', 'empresas_set')
