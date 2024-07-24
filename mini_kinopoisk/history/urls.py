from django.urls import path

from history.views import history


app_name = "history"


urlpatterns = [
    path("", history, name="index")
]
