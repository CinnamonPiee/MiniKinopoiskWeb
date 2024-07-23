from django.db import models
from users.models import User
from films_serials.models import SearchFilm, SearchSerial


class HistoryFilm(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    film = models.ForeignKey(to=SearchFilm, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self) -> str:
        return f"Film: {self.film.name} | User: {self.user.name}"


class HistorySerial(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    serial = models.ForeignKey(to=SearchSerial, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self) -> str:
        return f"Film: {self.serial.name} | User: {self.user.name}"
