from django.shortcuts import render, redirect
from portafolio_app.db.models import portafolio
from portafolio_app.db.models import tatuador

def load(request):

    if request.method == 'POST':
        # Obtener el ID del portafolio a eliminar
        portafolio_id = request.POST.get('portafolio_id')
        if portafolio_id:
            # Eliminar el portafolio
            portafolio.objects.filter(pk=portafolio_id).delete()
            # Redirigir a la misma página después de la eliminación
            return redirect('PerfilTatuador')
    tatuadores = tatuador.objects.all()
# Obtener todos los objetos del modelo Portafolio
    portafolios = portafolio.objects.all()
    # Pasar los objetos al contexto de la plantilla
    context = {'portafolios': portafolios, 'tatuadores' : tatuadores}
    # Renderizar la plantilla 'tatuador.html' con el contexto
    return render(request, 'PerfilTatuador.html', context)

