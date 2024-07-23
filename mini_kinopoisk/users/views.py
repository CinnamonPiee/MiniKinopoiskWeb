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
