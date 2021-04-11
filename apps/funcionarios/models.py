from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamneto
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamentos = models.ManyToManyField(Departamneto)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome
