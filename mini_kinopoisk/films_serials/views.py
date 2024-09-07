from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from .models import SearchFilm, SearchSerial


@login_required
def films_serials(request: HttpRequest):
    context = {
        "films": SearchFilm.objects.all(),
        "serials": SearchSerial.objects.all(),
    }
    
    return render(
        request,
        "films_serials/index.html",
        context,
    )
