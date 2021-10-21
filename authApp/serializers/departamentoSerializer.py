from authApp.models.departamento        import Departamento
from rest_framework                     import serializers


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Departamento
        fields = ['id', 'name']
    
    def create(self, validated_data):
        departamentoInstance = Departamento.objects.create(**validated_data)
        return departamentoInstance

    def to_representation(self, obj):
        departamento = Departamento.objects.get(id = obj.id)
        return {
            "id" : departamento.id,
            "name" : departamento.name
        }
