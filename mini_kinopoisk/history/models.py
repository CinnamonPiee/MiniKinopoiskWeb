from django.db import models
from users.models import Users
from films_serials.models import SearchFilm, SearchSerial


class HistoryFilm(models.Model):
    user_id = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    film_id = models.ForeignKey(to=SearchFilm, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class HistorySerial(models.Model):
    user_id = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    serial_id = models.ForeignKey(to=SearchSerial, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
