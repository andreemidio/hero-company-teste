from django.urls import path, include
from rest_framework import routers

from apps.empresas.viewsets import CriarEmpresaViewSet, GetEmpresaViewSet

app_name = 'empresas'

router = routers.DefaultRouter()
router.register(r'criar-empresas', CriarEmpresaViewSet, basename='criar-empresas')
router.register(r'buscar-empresas', GetEmpresaViewSet, basename='buscar-empresas')

urlpatterns = [
    path(r'', include(router.urls)),
]
