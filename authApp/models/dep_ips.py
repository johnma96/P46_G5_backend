from django.db      import models
from .ips           import Ips
from .departamento  import Departamento

class Dep_ips(models.Model):
    id              = models.AutoField(primary_key=True)
    ips             = models.ForeignKey(Ips, on_delete=models.CASCADE)
    departamento    = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    name            = models.CharField('Departamento-IPS', max_length = 30, unique=True)

