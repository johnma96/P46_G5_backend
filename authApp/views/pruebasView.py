from django.conf                                  import settings
from rest_framework                               import generics, status
from rest_framework.response                      import Response


from authApp.models.pruebas                import Pruebas
from authApp.serializers.pruebasSerializer import PruebasSerializer



class PruebasCreateView(generics.CreateAPIView):
    serializer_class   = PruebasSerializer

    def post(self, request, *args, **kwargs):
    
        serializer = PruebasSerializer(data=request.data['pruebas_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Prueba registrada", status=status.HTTP_201_CREATED)
