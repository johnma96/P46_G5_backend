from authApp.models.dep_ips             import Dep_ips
from authApp.models.ips                 import Ips
from authApp.models.departamento        import Departamento
from rest_framework                     import serializers

class Dep_ipsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Dep_ips
        fields = ['ips','departamento']

 