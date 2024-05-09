"""
URL configuration for portafolio_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# HABILITAR LOS DEMÁS MODEL DE DJANGO EN EL ADMIN
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


from .views import logout
from .views import loginpage
from .db.models import region, provincia, comuna
from .db.models import persona, emails, telefono, direccion, cliente
from .db.models import estudio, tatuador, reseña, portafolio, diseño
from .db.models import materiales, cita, factura, metodo_pago, transacciones, detalle_factura


# ADD MODEL IN ADMIN
admin.site.register(Permission)
admin.site.register(ContentType)
admin.site.register(region)
admin.site.register(provincia)
admin.site.register(comuna)
admin.site.register(persona)
admin.site.register(emails)
admin.site.register(telefono)
admin.site.register(direccion)
admin.site.register(cliente)
admin.site.register(estudio)
admin.site.register(tatuador)
admin.site.register(reseña)
admin.site.register(portafolio)
admin.site.register(diseño)
admin.site.register(materiales)
admin.site.register(cita)
admin.site.register(factura)
admin.site.register(metodo_pago)
admin.site.register(transacciones)
admin.site.register(detalle_factura)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout', logout.load),
    path('', admin.site.urls),  
    path('accounts/login/', loginpage.load),   
    path('loginpage',loginpage.load),
]
