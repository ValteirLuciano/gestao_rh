from django.db import models


class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome
