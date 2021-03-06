from django.conf                                  import settings
from django.core.exceptions                       import PermissionDenied
from rest_framework                               import generics, status
from rest_framework.permissions                   import IsAuthenticated
from rest_framework.response                      import Response
from rest_framework_simplejwt.backends            import TokenBackend
from datetime import date, datetime

from authApp.models.pruebas                import Pruebas
from authApp.serializers.pruebasSerializer import PruebasSerializer


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


class PruebaDetailView(generics.RetrieveAPIView):
    serializer_class   = PruebasSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Pruebas.objects.all()

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        data_return = super().get(request, *args, **kwargs)
        if data_return.data['dep_ips']['id'] !=  self.kwargs['user']:
            stringResponse = {'detail':"Unauthorized Request. You did't enter this test"}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return data_return

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
        
        startDate = self.request.query_params.get('startDate')
        endDate   = self.request.query_params.get('endDate')

        if startDate is not(None) and endDate is None:
            format = "%Y-%m-%d"
            dt_startDate = datetime.strptime(startDate, format)
            queryset = queryset.filter(testDate__date = dt_startDate.date())

        if startDate is not(None) and endDate is not(None):
            queryset = queryset.filter(testDate__range=[startDate, endDate])
                    
        return queryset

class PruebasDepartamentoView(generics.ListAPIView):
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
 
        queryset = Pruebas.objects.select_related('dep_ips__departamento').filter(dep_ips__departamento__name = self.kwargs['departamento'])
        # print('*'*100)
        # print(str(queryset.query))
        # print('*'*100)

        startDate = self.request.query_params.get('startDate')
        endDate   = self.request.query_params.get('endDate')

        if startDate is not(None) and endDate is None:
            format = "%Y-%m-%d"
            dt_startDate = datetime.strptime(startDate, format)
            queryset = queryset.filter(testDate__date = dt_startDate.date())

        if startDate is not(None) and endDate is not(None):
            queryset = queryset.filter(testDate__range=[startDate, endDate])
            
        return queryset

class PruebasIpsView(generics.ListAPIView):
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

        queryset = Pruebas.objects.select_related('dep_ips__ips').filter(dep_ips__ips__name = self.kwargs['ips'])
        # print('*'*100)
        # print(str(queryset.query))
        # print('*'*100)

        startDate = self.request.query_params.get('startDate')
        endDate   = self.request.query_params.get('endDate')

        if startDate is not(None) and endDate is None:
            format       = "%Y-%m-%d"
            dt_startDate = datetime.strptime(startDate, format)
            queryset     = queryset.filter(testDate__date = dt_startDate.date())

        if startDate is not(None) and endDate is not(None):
            queryset = queryset.filter(testDate__range=[startDate, endDate])

        return queryset


class PruebaUpdateView(generics.UpdateAPIView):
    serializer_class   = PruebasSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Pruebas.objects.all()

    def update(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        if (valid_data['user_id'] != self.kwargs['user']):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        detailTest = Pruebas.objects.get(id = self.kwargs['pk'])

        if (self.kwargs['user'] != detailTest.dep_ips_id):
            stringResponse = {'detail':'Unauthorized Request. You cannot change a test that you did not create'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        if request.data['dep_ips'] != detailTest.dep_ips_id:
            stringResponse = {'detail':'Unauthorized Request. You cannot transfer a test that you created'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        if not('testDate' in request.data):
            request.data['testDate'] = datetime.now()

        totalTests = request.data['positiveTests'] + request.data['negativeTests'] + request.data['indeterminateTests']
        request.data['totalTests'] = totalTests

        return super().update(request, *args, **kwargs)


class PruebaDeleteView(generics.DestroyAPIView):
    serializer_class   = PruebasSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Pruebas.objects.all()

    def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        detailTest = Pruebas.objects.get(id = self.kwargs['pk'])

        if (self.kwargs['user'] != detailTest.dep_ips_id):
            stringResponse = {'detail':'Unauthorized Request. You cannot delete a test that you did not create'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)