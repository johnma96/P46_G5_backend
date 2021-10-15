from django.conf                                  import settings
from rest_framework                               import views, status
from rest_framework.response                      import Response
from rest_framework.permissions                   import IsAuthenticated
#from rest_framework_simplejwt.backends            import TokenBackend

from authApp.serializers.departamentoSerializer import DepartamentoSerializer

class DepartamentoCreateView(views.APIView):
    serializer_class   = DepartamentoSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = DepartamentoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Departamento agregado exitosamente", status=status.HTTP_201_CREATED)