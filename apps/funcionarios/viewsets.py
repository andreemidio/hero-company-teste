from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.funcionarios.models import Funcionarios
from apps.funcionarios.serializers import PostFuncionariosSerializer, GetFuncionariosSerializer


class PostFuncionariosViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PostFuncionariosSerializer
    queryset = Funcionarios.objects.all()


class GetFuncionariosViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = GetFuncionariosSerializer
    queryset = Funcionarios.objects.all()
