from django.shortcuts import render

#          nombre de los archivos               nombre de la clase        
from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos, Empleados

# Create your views here.
#cada vista es una funcion de python

def Home(request):
    return render(request, 'index.html') 


def PlatosVista(request):
    # cargar el formulario de registro de platos
    formulario=FormularioRegistroPlatos()
    
    #creamos un diccionario para enviar datos hacia el template
    diccionariodeEnvioDatos={
        'formulario':formulario
    }

    #recibiendo datos del formulario
    #peticion de tipo posterior

    if request.method == 'POST':
        datosFormulario=FormularioRegistroPlatos(request.POST)
        """ print (datosFormulario) """
        #si los datos del formulario pasaron todos los filtos entonces limpiamos los datos
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print (datosLimpios)
            #enviando datos a la BD
            platoNuevo=Platos(
                nombre=datosLimpios["nombrePlato"],
                descripcion=datosLimpios["descripcionPlato"],
                imagen=datosLimpios["fotoPlato"],
                precio=datosLimpios["precioPlato"],
                tipo=datosLimpios["tipoPlato"]
            )
            platoNuevo.save()


    return render (request, 'platos.html', diccionariodeEnvioDatos)

def EmpleadosVista(request):
    formularioEmpleado=FormularioEmpleados()

    diccionarioEnvioDatosEmpleados={
        'formularioEmpleado':formularioEmpleado
    }

    if request.method == 'POST':
        datosFormularioEmpleados=FormularioEmpleados(request.POST)

        if datosFormularioEmpleados.is_valid():
            datosLimpios=datosFormularioEmpleados.cleaned_data
            print (datosLimpios)
            #enviando datos a la base de datos
            empleadoNuevo=Empleados(
                id=datosLimpios["idEmpleado"],
                nombreempleado=datosLimpios["nombreEmpleado"],
                apellidoempleado=datosLimpios["apellidoEmpleado"],
                cargoempleado=datosLimpios["cargoEmpleado"],
                direccionempleado=datosLimpios["direccionEmpleado"],
                salarioempleado=datosLimpios["salarioMensualEmpleado"]
            )
            empleadoNuevo.save()

    return render (request, 'empleados.html', diccionarioEnvioDatosEmpleados)
