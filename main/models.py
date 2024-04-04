from django.db import models
from django.db.models import SET_NULL

class Candidato(models.Model):
    cpf = models.CharField(max_length = 11, null = False, blank = False)
    nome = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    area_atuacao = models.CharField(max_length = 50)
    descricao = models.TextField(max_length = 255)

    def __str__(self) -> str:
        return self.nome

class Habilidades(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete = models.CASCADE)
    habilidade = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.habilidade

    class Meta:
        verbose_name_plural = "Habilidades"

class Recrutador(models.Model):
    nome = models.CharField(max_length = 50, null = False)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Recrutadores"

class Empresa(models.Model):
    cnpj = models.CharField(max_length=14, unique= True)
    nome_fantasia = models.CharField(max_length=50)
    ramo_empresarial = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    descricao = models.TextField(max_length = 255, null = True, blank = True)

    def __str__(self) -> str:
        return self.nome_fantasia

class Vaga(models.Model):
    titulo = models.CharField(max_length= 100, null = False)
    area = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    requisitos = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    recrutador = models.ForeignKey(Recrutador, null = True, blank = True, on_delete=SET_NULL)

    def __str__(self):
        return self.titulo
