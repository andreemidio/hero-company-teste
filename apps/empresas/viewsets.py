from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.empresas.models import Empresas
from apps.empresas.serializers import PostEmpresaSerializer, GetEmpresasSerializer


class CriarEmpresaViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PostEmpresaSerializer
    # queryset = Empresas.objects.all()


class GetEmpresaViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = GetEmpresasSerializer
    queryset = Empresas.objects.all()
