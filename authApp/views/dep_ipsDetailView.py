from django.conf                           import settings
from rest_framework                        import generics, status
from rest_framework.response               import Response
from rest_framework.permissions            import IsAuthenticated
from rest_framework_simplejwt.backends     import TokenBackend

from authApp.models.dep_ips                import Dep_ips
from authApp.serializers.dep_ipsSerializer import Dep_ipsSerializer


class Dep_ipsDetailView(generics.RetrieveAPIView):
    queryset           = Dep_ips.objects.all()
    serializer_class   = Dep_ipsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token         = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data    = token_backend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)