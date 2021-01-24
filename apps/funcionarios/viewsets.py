from rest_framework import mixins
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.viewsets import GenericViewSet

from apps.funcionarios.models import Funcionarios
from apps.funcionarios.serializers import PostFuncionariosSerializer, ListFuncionariosSerializer, \
    GetFuncionariosSerializer, GetFuncionariosEmpresasSerializer


class PostFuncionariosViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PostFuncionariosSerializer
    queryset = Funcionarios.objects.all()


class ListFuncionariosViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ListFuncionariosSerializer
    queryset = Funcionarios.objects.all()


class GetFuncionariosViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = GetFuncionariosSerializer
    queryset = Funcionarios.objects.all()


class GetFuncionariosEmpresasViewSet(RetrieveAPIView):
    queryset = Funcionarios.objects.all()
    serializer_class = GetFuncionariosEmpresasSerializer
    filter_fields = ['nome_sobrenome']

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=pk)
        return obj
