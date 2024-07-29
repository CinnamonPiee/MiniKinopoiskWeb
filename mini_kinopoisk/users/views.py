from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("users:profile"))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        "form": form
    }
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
            messages.success(request, "Поздравляем, вы успешно зарегистрированы!")
            return redirect(reverse("users:login"))
    else:
        form = UserRegistrationForm()
    context = {
        "form": form,
    }
    return render(request, "users/registration.html", context=context)


def logout(request):
    auth.logout(request)
    return redirect(reverse("main_page"))