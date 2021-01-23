from django.urls import path, include
from rest_framework import routers

from apps.funcionarios.viewsets import GetFuncionariosEmpresasViewSet
from apps.funcionarios.viewsets import GetFuncionariosViewSet
from apps.funcionarios.viewsets import ListFuncionariosViewSet
from apps.funcionarios.viewsets import PostFuncionariosViewSet

app_name = 'funcionarios'

router = routers.DefaultRouter()
router.register(r'criar-funcionarios', PostFuncionariosViewSet, basename='criar-funcionarios')
router.register(r'buscar-funcionarios', ListFuncionariosViewSet, basename='buscar-funcionarios')
router.register(r'detalhes-funcionario', GetFuncionariosViewSet, basename='detalhes-funcionario')
# router.register(r'detalhes-funcionario-empresa', GetFuncionariosEmpresasViewSet.as_view(),
#                 basename='detalhes-funcionario-empresa')

urlpatterns = [
    path(r'', include(router.urls)),
    path('detalhes-funcionario-empresa/', GetFuncionariosEmpresasViewSet.as_view(), name="detalhes-funcionario-empresa"),
]
