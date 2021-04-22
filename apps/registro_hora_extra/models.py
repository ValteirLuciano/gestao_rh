from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField('Motivo', max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField('Horas Extras', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'RegistroHoraExtra'
        verbose_name_plural = 'RegistroHoraExtras'

    def get_absolute_url(self):
        return reverse('update_hora_extra', args=[self.id])

    def __str__(self):
        return self.motivo
