from django.db      import models
from .ips           import User
from .departamento  import Departamento

class Dep_ips(models.Model):
    id              = models.AutoField(primary_key=True)
    userId          = models.ForeignKey(User, on_delete=models.CASCADE)
    departamentoId  = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    name            = models.CharField('Departamento-IPS', max_length = 30, unique=True)

