from authApp.models.dep_ips                     import Dep_ips
from authApp.models.ips                         import Ips
from authApp.serializers.ipsSerializer          import IpsSerializer
from authApp.models.departamento                import Departamento
from authApp.serializers.departamentoSerializer import DepartamentoSerializer
from authApp.models.pruebas                     import Pruebas
from authApp.serializers.pruebasSerializer      import PruebasSerializer

from rest_framework                             import serializers

class Dep_ipsSerializer(serializers.ModelSerializer):
    prueba = PruebasSerializer()
    class Meta:
        model  = Dep_ips
        fields = ['id', 'ips', 'departamento', 'name', 'username', 'password', 'prueba', 'ips', 'departamento']

    def create(self, validated_data):
        pruebaData = validated_data.pop('prueba')
        userInstance = Dep_ips.objects.create(**validated_data)
        Pruebas.objects.create(dep_ips=userInstance, **pruebaData)
        return userInstance

    def to_representation(self, obj):
        user = Dep_ips.objects.get(id=obj.id)
        prueba = Pruebas.objects.get(dep_ips=obj.id)
        #ips = Ips.objects.get(id=obj.id)
        #ips = Ips.objects.get(id=obj.id_ips)
        #departamento = Departamento.objects.get(id=obj.id_dep)

        return {
            "id"          : user.id,
            "username"    : user.username,
            "name"        : user.name,
            #"departamento": departamento.name,
            #"ips"         : ips.name,
            "prueba" : {
                "id"                 : prueba.id,
                "testDate"           : prueba.testDate,
                "positiveTests"      : prueba.positiveTests,
                "negativeTests"      : prueba.negativeTests,
                "indeterminateTests" : prueba.indeterminateTests,
                "totalTests"         : prueba.totalTests
            }
        }


 