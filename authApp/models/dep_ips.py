from django.db      import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


from .ips           import Ips
from .departamento  import Departamento


class Dep_ips(AbstractBaseUser, PermissionsMixin):
    id           = models.BigAutoField(primary_key=True)
    ips          = models.ForeignKey(Ips, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    name       = models.CharField('IPS-Departamento', max_length = 50, unique=True)
    username      = models.CharField('Usuario', max_length=30, unique=True)
    password        = models.CharField('Clave', max_length=256)

    def save(self, **kwargs):
        some_salt = 'mJAFM15safai342akAA88KisJ8'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)


