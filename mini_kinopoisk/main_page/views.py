from django.shortcuts import render


def main_page(request):
    return render(
        request,
        "main_page/index.html",
        {"title": "Mini Kinopoisk"},
    )
