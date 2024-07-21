from django.shortcuts import render


def films_serials(request):
    return render(
        request,
        "films_serials/index.html",
        {"title": "Mini Kinopoisk"},
    )
