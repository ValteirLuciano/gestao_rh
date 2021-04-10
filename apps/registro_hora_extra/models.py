from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField('Motivo', max_length=100)

    class Meta:
        verbose_name = 'RegistroHoraExtra'
        verbose_name_plural = 'RegistroHoraExtras'

    def __str__(self):
        return self.motivo
