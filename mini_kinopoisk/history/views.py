from django.shortcuts import render


def history(request):
    context = {}
    return render(
        request,
        "history/index.html",
        context,
    )
