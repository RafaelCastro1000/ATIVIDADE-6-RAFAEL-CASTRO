from django.db import models

class Trofeus(models.Model):
  nome = models.CharField(max_length = 50)
  data = models.DateField()
  descricao = models.TextField()

class Jogadores(models.Model):
  nome = models.CharField(max_length = 50)
  posicao = models.CharField(max_length=50)
  numero_camisa = models.CharField(max_length=3)
  caracteristicas = models.TextField()
  aprovação = models.BooleanField()
  