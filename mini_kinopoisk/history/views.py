from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from .models import HistoryFilm, HistorySerial


@login_required
def history(request: HttpRequest):
    context = {
        "history_film": HistoryFilm.objects.all(),
        "history_serial": HistorySerial.objects.all(),
    }
    
    return render(
        request,
        "history/index.html",
        context,
    )
