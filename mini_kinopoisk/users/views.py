from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm


def user(request):
    context = {}
    return render(request, "users/profile.html", context=context)


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse("main_page"))
    else:
        form = UserLoginForm()
    context = {
        "form": form,
    }
    return render(request, "users/login.html", context=context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("main_page"))
    else:
        form = UserRegistrationForm()
    context = {
        "form": form,
    }
    return render(request, "users/registration.html", context=context)
