from django.conf                                import settings
from rest_framework                             import generics, status
from rest_framework.response                    import Response
from rest_framework.permissions                 import IsAuthenticated
from rest_framework_simplejwt.backends          import TokenBackend

from authApp.models                             import Departamento     
from authApp.serializers.departamentoSerializer import DepartamentoSerializer

class DepartamentoCreateView(generics.RetrieveAPIView):
    serializer_class   = DepartamentoSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = DepartamentoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Departamento agregado exitosamente", status=status.HTTP_201_CREATED)

class DepartamentoListView(generics.ListAPIView):
    serializer_class   = DepartamentoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        queryset = Departamento.objects.all()
        return queryset