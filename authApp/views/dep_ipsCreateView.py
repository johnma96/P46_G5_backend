from rest_framework                           import status, views
from rest_framework.response                  import Response
from rest_framework_simplejwt.serializers     import TokenObtainPairSerializer
from authApp.serializers.dep_ipsSerializer    import Dep_ipsSerializer

class Dep_ipsCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        #Agrego esta línea al request para engañar al código y simular que en el request
        #viene un dep_ips, pero luego, ese argumento se corta en el dep_ips serializer
        request.data['prueba']['dep_ips'] = 1 

        serializer = Dep_ipsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"username":request.data["username"],
                     "password":request.data["password"]}
        try:
            tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            tokenSerializer.is_valid(raise_exception=True)
            return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response('Error in token generation', status=status.HTTP_500_INTERNAL_SERVER_ERROR)