from authApp.models.pruebas        import Pruebas
from authApp.models.dep_ips        import Dep_ips
from authApp.models.ips            import Ips
from authApp.models.departamento   import Departamento
from rest_framework                import serializers

from dateutil.tz import gettz

class PruebasSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Pruebas
        fields = ['testDate', 'positiveTests', 'negativeTests','indeterminateTests','totalTests', 'dep_ips']#'dep_ips', 

    def create(self, validated_data):
        pruebasInstance = Pruebas.objects.create(**validated_data)
        return pruebasInstance

    def to_representation(self, obj):

        prueba       = Pruebas.objects.get(id=obj.id)
        dep_ips      = Dep_ips.objects.get(id=obj.dep_ips_id)
        ips          = Ips.objects.get(id=dep_ips.ips_id)
        departamento = Departamento.objects.get(id=dep_ips.departamento_id)
        zone         = 'America/Bogota'
        dtZone       = prueba.testDate.astimezone(gettz(zone)).isoformat(sep=' ')[:-6]

        return {
            'id'                 : prueba.id,
            'testDate'           : dtZone,
            'positiveTests'      : prueba.positiveTests,
            'negativeTests'      : prueba.negativeTests,
            'indeterminateTests' : prueba.indeterminateTests,
            'totalTests'         : prueba.totalTests,
            'dep_ips': {
                'id'          : dep_ips.id,
                'departamento': departamento.name, 
                'ips'         : ips.name
            }
        }

