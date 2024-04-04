from rest_framework import serializers
from main.models import Candidato, Habilidades, Vaga, Recrutador, Empresa


class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'

class HabilidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidades
        fields = '__all__'

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'

class RecrutadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recrutador
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
        