from django.contrib import admin
from .models import Departamneto


@admin.register(Departamneto)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
