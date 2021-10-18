from django.contrib                 import admin
from django.urls                    import path
from authApp                        import views  as authAppViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('admin/',                                  admin.site.urls),  # use defaul Djando Admin
    path('ips/list/',                               authAppViews.IpsListView.as_view()), # get list of IPSs  
    path('ips/create/',                             authAppViews.IpsCreateView.as_view())  , #create a new ips
    path('departamento/list/',                      authAppViews.DepartamentoListView.as_view()),
    path('departamento/create/',                    authAppViews.DepartamentoCreateView.as_view()), #create a new departamento    
    path('dep_ips/',                                authAppViews.Dep_ipsCreateView.as_view()), # create a new dep_ips
    path('dep_ips/<int:pk>/',                       authAppViews.Dep_ipsDetailView.as_view()), # check info for an specific dep_ips based on id(pk)   
    path('prueba/create/',                          authAppViews.PruebasCreateView.as_view()), # create a new test for a specific dep_ips
    path('prueba/<int:user>/',                      authAppViews.PruebasDep_ipsView.as_view()), # Filter test by dep_ips
    path('prueba/ips/<str:ips>/',                   authAppViews.PruebasIpsView.as_view()),    #filter tests by IPS
    path('prueba/departamento/<str:departamento>/', authAppViews.PruebasDepartamentoView.as_view()), #filter tests by departamento
    path('prueba/update/<int:user>/<int:pk>/',      authAppViews.PruebaUpdateView.as_view()), # update a specific test
    path('prueba/delete/<int:user>/<int:pk>/',      authAppViews.PruebaDeleteView.as_view()), # delete a specific test
    path('login/',                                  TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',                                TokenRefreshView.as_view()), # generate new access token

]
