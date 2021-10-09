from authApp.models.pruebas        import Pruebas
from rest_framework                import serializers

class PruebasSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Pruebas
        fields = ['testDate', 'positiveTests', 'negativeTests','indeterminateTests','totalTests']

