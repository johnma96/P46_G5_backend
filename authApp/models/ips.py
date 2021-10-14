from django.db                   import models


class Ips(models.Model):
    id       = models.BigAutoField(primary_key=True)
    name     = models.CharField('IPS', max_length = 30, unique=True)
    password = models.CharField('Contraseña', max_length = 256)


    
prueba