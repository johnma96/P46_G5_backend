import django


from .dep_ips              import Dep_ips
from django.db             import models


class Pruebas(models.Model):
    id                  = models.AutoField(primary_key=True)
    dep_ips             = models.ForeignKey(Dep_ips, related_name='pruebas', on_delete=models.CASCADE)
    testDate            = models.DateTimeField(default=django.utils.timezone.now)
    positiveTests       = models.IntegerField(default=0)
    negativeTests       = models.IntegerField(default=0)
    indeterminateTests  = models.IntegerField(default=0)
    totalTests          = models.IntegerField(default=0)
