from django.shortcuts import render


def history(request):
    return render(
        request,
        "history/index.html",
        {"title": "Mini Kinopoisk"},
    )
