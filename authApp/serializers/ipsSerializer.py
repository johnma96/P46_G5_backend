from rest_framework                        import serializers
from authApp.models.ips                    import Ips

class IpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ips
        fields = ['id', 'name']

    def create(self, validated_data):
        ipsInstance = Ips.objects.create(**validated_data)
        return ipsInstance   

    def to_representation(self, obj):
        ips    = Ips.objects.get(id=obj.id)
        return {
            'id'      : ips.id,
            'name'    : ips.name,
        }

