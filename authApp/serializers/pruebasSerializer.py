from authApp.models.pruebas        import Pruebas
from authApp.models.ips            import Ips
from authApp.models.departamento   import Departamento
from rest_framework                import serializers

class PruebasSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Pruebas
        fields = ['testDate', 'positiveTests', 'negativeTests','indeterminateTests','totalTests']

    def to_representation(self, obj):
        ips          = Ips.objects.get(id=obj.id)
        departamento = Departamento.objects.get(id=obj.id)
        pruebas      = Pruebas.objects.get(id=obj.id)
        return {
            'id'                 : pruebas.id,
            'testDate'           : pruebas.testDate,
            'positiveTests'      : pruebas.positiveTests,
            'negativeTests'      : pruebas.note,
            'indeterminateTests' : pruebas.note,
            'ips' : {
                'id'   : ips.id,
                'name' : ips.name
            },
            'departamento' : {
                'id'    : departamento.id,
                'name'  : departamento.name,
            }
        }    

