from rest_framework import serializers

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
