from rest_framework                        import serializers
from authApp.models.ips                    import User
from authApp.models.pruebas                import Pruebas
from authApp.serializers.pruebasSerializer import PruebasSerializer

class UserSerializer(serializers.ModelSerializer):
    pruebas = PruebasSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'pruebas']
        
    def create(self, validated_data):
        pruebasData  = validated_data.pop('pruebas')
        userInstance = User.objects.create(**validated_data)
        Pruebas.objects.create(user=userInstance, **pruebasData)
        return userInstance

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        pruebas = Pruebas.objects.get(user=obj.id)
        return {
            'id'      : user.id,
            'username': user.username,
            'pruebas' : {
                'id'                 : pruebas.id,
                'testDate'           : pruebas.testDate,
                'positiveTests'      : pruebas.positiveTests,
                'negativeTests'      : pruebas.negativeTests,
                'indeterminateTests' : pruebas.indeterminateTests,
                'totalTests'         : pruebas.totalTests
            }
        }

