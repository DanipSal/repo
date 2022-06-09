from django.urls import path
from . import views



urlpatterns = [
    
    path('', views.inicio),
    path('Pacientes', views.Pacientes , name='Pacientes'),
    path('Medico', views.Medico , name='Medico'),
    path('Turnos', views.Turnos , name= 'Turnos'),
    path('contacto', views.contacto , name='contacto'),
    path('alta_paciente' , views.alta_paciente ),
    path('alta_medico' , views.alta_medico),
    path('alta_turno' , views.alta_turno),
    path('busquedas' , views.busquedas),
    path('resultado_busqueda' , views.resultado_busqueda)
    
]