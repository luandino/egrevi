"""egrevi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from egrevi.views import saludos, despedida, dame_fecha, calcula_edad, calcula_jubilacion, estudios, cursop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tesaludo/', saludos),
    path('despedida/', despedida),
    path('fecha/', dame_fecha),
    path('edad/<int:anio>', calcula_edad),
    path('edadanio/<int:edad>/<int:anio>', calcula_edad),
    path('plantilla/', calcula_jubilacion),
    path('estudios/', estudios),
    path('cursop/', cursop)
]
