from django.shortcuts import render
from portafolio_app.db.models import reseña

def load(request):
# Obtener todos los objetos del modelo Reseñas
    reseñas = reseña.objects.all()
    # Pasar los objetos al contexto de la plantilla
    context = {'reseñas': reseñas}
    # Renderizar la plantilla 'tatuador.html' con el contexto
    return render(request, 'ReseñasPage.html', context)