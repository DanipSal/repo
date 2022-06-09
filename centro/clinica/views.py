from django.http import HttpResponse
from django.shortcuts import render
from clinica.models import Pacientes
from clinica.models import Medico
from clinica.models import Turnos
from django.template import loader
from clinica.forms import Pacientes_formulario , Medico_formulario , Turnos_formulario
import datetime  

# Create your views here.


def inicio(request):
    return render(request, "plantillas.html")

def Pacientes(request):
    paciente= Pacientes
    dicc = {"paciente" : paciente}
    plantilla = loader.get_template("Pacientes.html")
    documento = plantilla.render(dicc)
    return render (request, 'Pacientes.html')

def alta_pacientes( request , nombre):
    usuario = Pacientes(nombre= "nombre", edad="28" , nacimiento="25122002" )
    usuario.save()
    texto = f"Se guardo en la BD el paciente: {Pacientes.nombre} Edad: {Pacientes.edad} Nacimiento: {Pacientes.nacimiento}"
    return HttpResponse(texto)


def Medico(request):
    return render (request, 'alta_medico.html')

def Turnos(request):
    return render (request, 'Turnos.html')

def contacto(request):

    return render( request , "contacto.html" )  


def alta_paciente(request):

    return render (request, 'formulario.html')
    
    
    if request.method == "POST":

        mi_formulario =  Pacientes_formulario (request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            usuario = Pacientes(nombre=datos["nombre"] , DNI=datos["DNI"] , nacimiento=datos["nacimiento"])
            usuario.save()

            return render(request , "formulario.html")
   
 




def alta_medico(request):
    
    if request.method == "POST":

        mi_formulario =  Medico_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            doctor = Medico(medico=datos["medico"], especialidad=datos["especialidad"]) 
            doctor.save()
           
    return render (request,'alta_medico.html')


def alta_turno(request):
    
    if request.method == "POST":

        mi_formulario =  Turnos_formulario (request.POST)

        if mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data
            fecha= Turnos(fechaturno=datos["fechaturno"], especialidad=datos["especialidad"]) 
            fecha.save()

            return HttpResponse("TURNO ASIGNADO")
           
    return render (request,'alta_turno.html')

def busquedas (request):
    return render (request , "busquedas.html")

def resultado_busqueda(request):

    if request.GET['medico']:

        medico = request.GET['medico']

        medicos = Medico.objects.filter(medico__icontains = medico)
        
        return render (request, "resultado_busqueda.html" , { "medicos" : medicos })

        
    else:
        return HttpResponse("SIN DATOS")






    

