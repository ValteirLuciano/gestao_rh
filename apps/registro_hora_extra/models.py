from django.db import models
from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField('Motivo', max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'RegistroHoraExtra'
        verbose_name_plural = 'RegistroHoraExtras'

    def __str__(self):
        return self.motivo
