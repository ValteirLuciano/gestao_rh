# Generated by Django 2.2.9 on 2021-04-14 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_auto_20210410_0216'),
        ('funcionarios', '0003_auto_20210412_0930'),
        ('departamentos', '0003_departamneto_empresa'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Departamneto',
            new_name='Departamento',
        ),
    ]
