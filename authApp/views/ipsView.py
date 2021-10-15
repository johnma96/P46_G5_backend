from django.conf                                  import settings
from rest_framework                               import views, status
from rest_framework.response                      import Response
from rest_framework.permissions                   import IsAuthenticated
#from rest_framework_simplejwt.backends            import TokenBackend

from authApp.serializers.ipsSerializer import IpsSerializer

class IpsCreateView(views.APIView):
    serializer_class   = IpsSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = IpsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Ips agregada exitosamente", status=status.HTTP_201_CREATED)







