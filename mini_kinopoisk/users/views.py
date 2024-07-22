from django.shortcuts import render


def users(request):
    context = {}
    return render(
        request,
        "users/index.html",
        context,
    )
