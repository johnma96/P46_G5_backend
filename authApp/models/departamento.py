from django.db import models


class Departamento(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField('Departamento', max_length = 30, unique=True)

