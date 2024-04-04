from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import CandidatoViewSet, HabilidadesViewSet, VagaViewSet, RecrutadorViewSet, EmpresaViewSet

router = routers.DefaultRouter()
router.register('candidatos', CandidatoViewSet)
router.register('habilidades', HabilidadesViewSet)
router.register('vagas', VagaViewSet)
router.register('recrutadores', RecrutadorViewSet)
router.register('empresas', EmpresaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(router.urls)),
]
