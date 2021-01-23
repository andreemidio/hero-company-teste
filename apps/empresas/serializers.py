from rest_framework import serializers

from apps.empresas.models import Empresas


class PostEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ('id', 'cnpj', 'razao_social')


class GetEmpresasSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    cnpj = serializers.CharField(required=True)
    razao_social = serializers.CharField(required=True)
    data_criacao = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Empresas
        fields = ('id', 'cnpj', 'razao_social', 'data_criacao')
