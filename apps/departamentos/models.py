from django.db import models


class Departamneto(models.Model):
    nome = models.CharField('Nome', max_length=70)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nome
