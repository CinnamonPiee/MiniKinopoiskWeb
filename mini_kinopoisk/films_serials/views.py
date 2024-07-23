from django.shortcuts import render

from .models import SearchFilm, SearchSerial


def films_serials(request):
    context = {
        "films": SearchFilm.objects.all(),
        "serials": SearchSerial.objects.all(),
    }
    
    return render(
        request,
        "films_serials/index.html",
        context,
    )
