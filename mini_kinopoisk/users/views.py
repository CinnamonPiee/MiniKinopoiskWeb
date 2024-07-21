from django.shortcuts import render


def users(request):
    return render(
        request,
        "users/index.html",
        {"title": "Mini Kinopoisk"},
    )
