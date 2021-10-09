from django.contrib import admin
from .models.ips           import User
from .models.departamento  import Departamento
from .models.dep_ips       import Dep_ips
from .models.pruebas       import Pruebas

# Register your models here.
admin.site.register(User)
admin.site.register(Departamento)
admin.site.register(Dep_ips)
admin.site.register(Pruebas)
