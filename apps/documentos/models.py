from django.db import models


class Documento(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return self.descricao
