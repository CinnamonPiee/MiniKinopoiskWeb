from django.urls import path

from users.views import user, login, registration


app_name = "users"


urlpatterns = [
    path("", user, name="profile"),
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
]
