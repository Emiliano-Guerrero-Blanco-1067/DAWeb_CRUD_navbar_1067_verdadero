from django.urls import path
from clientes_app import views
urlpatterns = [
    path('clientes',views.inicio_vistaClientes,name='clientes'),
    path('registrarCliente/',views.registrarCliente,  name='registrarCliente'),
    path('seleccionarCliente/<id_cli>',views.seleccionarCliente,name="seleccionarCliente"),
    path('editarCliente/',views.editarCliente,name="editarCliente"),
    path("borrarCliente/<id_cli>",views.borrarCliente,name="borrarCliente")

]