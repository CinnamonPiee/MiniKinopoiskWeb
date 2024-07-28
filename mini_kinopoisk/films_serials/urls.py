from django.urls import path, include

from films_serials.views import films_serials


app_name = "films_serials"


urlpatterns = [
    path("", films_serials, name="index")
]