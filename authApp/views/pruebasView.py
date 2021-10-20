from django.conf                                  import settings
from django.core.exceptions                       import PermissionDenied
from rest_framework                               import generics, status
from rest_framework.permissions                   import IsAuthenticated
from rest_framework.response                      import Response
from rest_framework_simplejwt.backends            import TokenBackend


from authApp.models.pruebas                import Pruebas
from authApp.models.ips                    import Ips
from authApp.models.dep_ips                import Dep_ips
from authApp.serializers.pruebasSerializer import PruebasSerializer
from authApp.serializers.ipsSerializer     import IpsSerializer



class PruebasCreateView(generics.CreateAPIView):
    serializer_class   = PruebasSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        request.data['prueba_data']['dep_ips'] = request.data['user_id']

        totalTests = request.data['prueba_data']['positiveTests'] + request.data['prueba_data']['negativeTests'] + request.data['prueba_data']['indeterminateTests']
        request.data['prueba_data']['totalTests'] = totalTests

        serializer = PruebasSerializer(data=request.data['prueba_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Prueba registrada", status=status.HTTP_201_CREATED)

class PruebasDep_ipsView(generics.ListAPIView):
    serializer_class   = PruebasSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            raise PermissionDenied()
            # stringResponse = {'detail':'Unauthorized Request'}
            # return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        queryset = Pruebas.objects.filter(dep_ips_id=self.kwargs['user'])
        return queryset

class PruebasDepartamentoView(generics.ListAPIView):
    serializer_class = PruebasSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        # if valid_data['user_id'] != self.kwargs['user']:
        #     raise PermissionDenied()
            # stringResponse = {'detail':'Unauthorized Request'}
            # return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        
        #queryset = Pruebas.objects.select_related().filter(dep_ips__departamento__id = self.kwargs['user'])
        queryset = Pruebas.objects.select_related('dep_ips__departamento').filter(dep_ips__departamento__name = self.kwargs['departamento'])
        # print('*'*100)
        # print(str(queryset.query))
        # print('*'*100)

        return queryset

class PruebasIpsView(generics.ListAPIView):
    serializer_class = PruebasSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        # if valid_data['user_id'] != self.kwargs['user']:
        #     raise PermissionDenied()
            # stringResponse = {'detail':'Unauthorized Request'}
            # return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Pruebas.objects.select_related('dep_ips__ips').filter(dep_ips__ips__name = self.kwargs['ips'])
        # print('*'*100)
        # print(str(queryset.query))
        # print('*'*100)

        return queryset

class PruebaUpdateView(generics.UpdateAPIView):
    serializer_class = PruebasSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Pruebas.objects.all()
    #print(queryset, 'here'*100)

    def update(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['user']:# or request.data['dep_ips'] != valid_data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        totalTests = request.data['positiveTests'] + request.data['negativeTests'] + request.data['indeterminateTests']
        request.data['totalTests'] = totalTests

        return super().update(request, *args, **kwargs)

class PruebaDeleteView(generics.DestroyAPIView):
    serializer_class = PruebasSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Pruebas.objects.all()

    def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)
