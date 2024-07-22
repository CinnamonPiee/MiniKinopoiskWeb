from django.shortcuts import render


def films_serials(request):
    context = {}
    return render(
        request,
        "films_serials/index.html",
        context,
    )
