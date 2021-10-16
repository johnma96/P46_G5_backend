from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.contrib.auth.hashers import make_password


from .ips           import Ips
from .departamento  import Departamento


class Dep_ipsManager(BaseUserManager):
    def create_dep_ips(self, username, password=None):
        if not username:
            raise ValueError('La dep-ips debe tener un nickname o nombre de usuario')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superdep_ips(self, username, password):
        user = self.create_dep_ips(
            username=username,
            password=password
        )
        user.is_admin=True
        user.save(using=self.db)
        return user


class Dep_ips(AbstractBaseUser, PermissionsMixin):
    id           = models.BigAutoField(primary_key=True)
    ips          = models.ForeignKey(Ips, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    name         = models.CharField('IPS-Departamento', max_length = 50, unique=True)
    username     = models.CharField('Usuario', max_length=30, unique=True)
    password     = models.CharField('Clave', max_length=256)

    def save(self, **kwargs):
        some_salt = 'mJAFM15safai342akAA88KisJ8'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'


