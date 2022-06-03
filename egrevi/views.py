from django.http import HttpResponse
from django.template import Template, Context

import datetime


def estudios(request):
    #doc_externo=open(egrevi/plantillas/miplantilla.html)

    nombre="Luciano Andino"
    doc_externo=open("C:/Users/landino/PycharmProjects/egrevi/egrevi/plantillas/miplantillaloop.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    fecha_actual = datetime.datetime.now()
    actividades= ["Correr","Cocinar", "Enseñar"]
    #actividades=[]
    ctx=Context({"nombre_persona": nombre, "instante": fecha_actual, "conocimiento": actividades})
    documento=plt.render(ctx)
    return HttpResponse(documento)

def calcula_jubilacion(request):
    #doc_externo=open(egrevi/plantillas/miplantilla.html)

    nombre="Josecito"
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

