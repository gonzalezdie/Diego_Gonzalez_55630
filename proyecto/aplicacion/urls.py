from django.urls import path, include  
from django.contrib.auth.views import LogoutView
from .views import *
from django.conf import settings


urlpatterns = [
    path('', home, name= 'home' ),

    path('venta/', venta, name= 'venta' ),
    path('create_venta/', VentaCreate.as_view(), name= 'create_venta'), 
    path('update_venta/<int:pk>/', VentaUpdate.as_view(), name="update_venta"),
    path('delete_venta/<int:pk>/', VentaDelete.as_view(), name="delete_venta"),


    path('alquiler/', alquiler, name='alquiler'),
    path('create_alquiler/', AlquilerCreate.as_view(), name= 'create_alquiler'), 
    path('update_alquiler/<int:pk>/', AlquilerUpdate.as_view(), name="update_alquiler"),
    path('delete_alquiler/<int:pk>/', AlquilerDelete.as_view(), name="delete_alquiler"),

    path('inversiones/', inversiones , name= 'inversiones' ),
    path('inversiones_create/', InversionCreate.as_view(), name= 'create_inversiones' ),
    path('update_inversiones/<int:pk>/', InversionUpdate.as_view(), name='update_inversiones'),
    path('delete_inversiones/<int:pk>/', InversionDelete.as_view(), name= 'delete_inversiones' ),  
    
    path('asesores/', asesores, name= 'asesores' ),
    path('asesores_create/', AsesorCreate.as_view(), name= 'create_asesor' ), 
    path('update_asesores/<int:pk>/', AsesorUpdate.as_view(), name="update_asesor" ),
    path('delete_asesores/<int:pk>/', AsesorDelete.as_view(), name="delete_asesor" ),

    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('registro/', register , name="registro" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
    
    path('search/', search, name="search"),
    path('about/', about, name="about" ),
     
]

 
