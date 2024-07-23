from django.shortcuts import render

from .models import HistoryFilm, HistorySerial


def history(request):
    context = {
        "history_film": HistoryFilm.objects.all(),
        "history_serial": HistorySerial.objects.all(),
    }
    
    return render(
        request,
        "history/index.html",
        context,
    )
