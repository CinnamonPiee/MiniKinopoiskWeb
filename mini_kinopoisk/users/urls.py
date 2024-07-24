from django.urls import path

from users.views import users, login, registration


app_name = "users"


urlpatterns = [
    path("", users, name="index"),
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
]
