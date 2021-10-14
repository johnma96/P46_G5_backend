# from rest_framework                        import serializers
# from authApp.models.ips                    import Ips
# from authApp.models.pruebas                import Pruebas
# from authApp.serializers.pruebasSerializer import PruebasSerializer

# class IpsSerializer(serializers.ModelSerializer):
#     pruebas = PruebasSerializer()
#     class Meta:
#         model = Ips
#         fields = ['id', 'name', 'password', 'pruebas']
        

#     def to_representation(self, obj):
#         ips    = Ips.objects.get(id=obj.id)
#         pruebas = Pruebas.objects.get(ips=obj.id)
#         return {
#             'id'      : ips.id,
#             'name'    : ips.name,
#             'pruebas' : {
#                 'id'                 : pruebas.id,
#                 'testDate'           : pruebas.testDate,
#                 'positiveTests'      : pruebas.positiveTests,
#                 'negativeTests'      : pruebas.negativeTests,
#                 'indeterminateTests' : pruebas.indeterminateTests,
#                 'totalTests'         : pruebas.totalTests
#             }
#         }

