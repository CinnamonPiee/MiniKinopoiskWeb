from django.shortcuts import render

from .models import User


def users(request):
    context = {
        "users": User.objects.all(),
    }
    
    return render(
        request,
        "users/index.html",
        context,
    )


def login(request):
    return render(request, "users/login.html")


def registration(request):
    return render(request, "users/registration.html")