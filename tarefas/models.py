from django.db import models

# Create your models here.
class Tarefa(models.Model):
    tarefa = models.CharField(max_length=200)
    status = models.CharField(default='Ativa', max_length=10)
    btn = models.CharField(default='Concluir', max_length=10)
