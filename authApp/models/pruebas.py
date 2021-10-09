from django.db      import models
from .dep_ips       import Dep_ips

class Pruebas(models.Model):
    id                  = models.AutoField(primary_key=True)
    user                = models.ForeignKey(Dep_ips, on_delete=models.CASCADE)
    testDate            = models.DateTimeField()
    positiveTests       = models.IntegerField(default=0)
    negativeTests       = models.IntegerField(default=0)
    indeterminateTests  = models.IntegerField(default=0)
    totalTests          = models.IntegerField(default=0)
