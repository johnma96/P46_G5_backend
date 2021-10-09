from authApp.models.dep_ips             import Departamento
from rest_framework                     import serializers

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Departamento
        fields = ['user','departamento','name']