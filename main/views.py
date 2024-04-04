from rest_framework import viewsets
from main.models import Candidato, Habilidades, Vaga, Recrutador, Empresa
from main.serializers import CandidatoSerializer, HabilidadesSerializer, VagaSerializer, RecrutadorSerializer, EmpresaSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

class HabilidadesViewSet(viewsets.ModelViewSet):
    queryset = Habilidades.objects.all()
    serializer_class = HabilidadesSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

class RecrutadorViewSet(viewsets.ModelViewSet):
    queryset = Recrutador.objects.all()
    serializer_class = RecrutadorSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

