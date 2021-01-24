from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.funcionarios.models import Funcionarios
from apps.funcionarios.serializers import PostFuncionariosSerializer, ListFuncionariosSerializer, \
    GetFuncionariosEmpresasSerializer


class PostFuncionariosViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PostFuncionariosSerializer
    queryset = Funcionarios.objects.all()


class ListFuncionariosViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ListFuncionariosSerializer
    queryset = Funcionarios.objects.all()


class GetFuncionariosViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = GetFuncionariosEmpresasSerializer
    queryset = Funcionarios.objects.all()
