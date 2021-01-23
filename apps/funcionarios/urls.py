from django.urls import path, include
from rest_framework import routers

from apps.funcionarios.viewsets import PostFuncionariosViewSet, GetFuncionariosViewSet

app_name = 'funcionarios'

router = routers.DefaultRouter()
router.register(r'criar-funcionarios', PostFuncionariosViewSet, basename='criar-funcionarios')
router.register(r'buscar-funcionarios', GetFuncionariosViewSet, basename='buscar-funcionarios')

urlpatterns = [
    path(r'', include(router.urls)),
]
