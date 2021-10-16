from django.contrib                 import admin
from django.urls                    import path
from authApp                        import views  as authAppViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('admin/',              admin.site.urls),  # use defaul Djando Admin
    path('ips/',                authAppViews.IpsCreateView.as_view())  , #create a new ips
    path('departamento/',       authAppViews.DepartamentoCreateView.as_view()), #create a new departamento
    path('dep_ips/',            authAppViews.Dep_ipsCreateView.as_view()), # create a new dep_ips
    path('prueba/create',       authAppViews.PruebasCreateView.as_view()),
    path('dep_ips/<int:pk>/',   authAppViews.Dep_ipsDetailView.as_view()), # check info for an specific dep_ips based on id(pk)
    path('login/',              TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',            TokenRefreshView.as_view()), # generate new access token
]
