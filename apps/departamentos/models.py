from django.db import models
from django.urls import reverse

from apps.empresas.models import Empresa


class Departamento(models.Model):
    nome = models.CharField('Nome', max_length=70)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nome
