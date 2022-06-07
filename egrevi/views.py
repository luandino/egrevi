from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

import datetime


def cursop(request):

    fecha_actual = datetime.datetime.now()
    return render(request, "cursop.html",{"dame_fecha": fecha_actual})


def estudios(request):
    #doc_externo=open(egrevi/plantillas/miplantilla.html)

    nombre="Luciano Andino"
    #nombre="Profesor Juan"
    #doc_externo=open("C:/Users/landino/PycharmProjects/egrevi/egrevi/plantillas/miplantillaloop.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()

    doc_externo=get_template('miplantillaloop.html')


    fecha_actual = datetime.datetime.now()
    actividades= ["Correr","Cocinar", "Enseñar","Lavar los platos", "Macanear"]
    #actividades=[]
    #ctx=Context({"nombre_persona": nombre, "instante": fecha_actual, "conocimiento": actividades})
    #documento=doc_externo.render({"nombre_persona": nombre, "instante": fecha_actual, "conocimiento": actividades})
    #return HttpResponse(documento)
    return render(request,"miplantillaloop.html",{"nombre_persona": nombre, "instante": fecha_actual, "conocimiento": actividades})

def calcula_jubilacion(request):
    #doc_externo=open(egrevi/plantillas/miplantilla.html)

    nombre="Josecitow"
    doc_externo=open("C:/Users/landino/PycharmProjects/egrevi/egrevi/plantillas/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    fecha_actual = datetime.datetime.now()
    ctx=Context({"nombre_persona": nombre, "instante": fecha_actual})
    documento=plt.render(ctx)
    return HttpResponse(documento)

def calcula_edad(request, anio):
    edadActual=45
    periodo=anio-2019
    edadFutura=edadActual+periodo
    documento="""<html><body><h2>En el año %s tendr&aacute;s %s a&ntilde;os</body></html>"""%(anio, edadFutura)
    return HttpResponse(documento)

def calcula_edad(request, edad, anio):
    edadActual=edad
    suma=anio-2022
    edadFutura=edadActual+suma
    documento="""<html><body><h2>En el año %s tendr&aacute;s %s a&ntilde;os</body></html>"""%(anio, edadFutura)
    return HttpResponse(documento)

def dame_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento = """<html>
                       <body>
                           <h2>
                           Fecha y hora actuales %s
                           </h2>
                       </body>
                   </html>
                """ % fecha_actual
    return HttpResponse(documento)



def saludos(request): #primera vista
    documento="""<html>
                    <body>
                        <h1>
                        Saludo
                        </h1>
                    </body>
                </html>
                """
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("Despedida")

