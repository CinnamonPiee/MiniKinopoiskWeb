from django.db import models


class SearchFilm(models.Model):
    name = models.CharField(max_length=60, null=True)
    janr = models.CharField(max_length=60, null=True)
    year = models.IntegerField(null=True)
    country = models.CharField(null=True)
    movie_length = models.PositiveIntegerField(null=True)
    description = models.TextField(null=True)
    rating = models.FloatField(null=True)
    age_rating = models. PositiveBigIntegerField(null=True)
    picture = models.URLField(max_length=200, null=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self) -> str:
        return self.name


class SearchSerial(models.Model):
    name = models.CharField(max_length=60, null=True)
    janr = models.CharField(max_length=60, null=True)
    rating = models.FloatField(null=True)
    release_year = models.CharField(max_length=60, null=True)
    series_length = models.CharField(max_length=10, null=True)
    country = models.CharField(null=True)
    age_rating = models. PositiveBigIntegerField(null=True)
    description = models.TextField(null=True)
    picture = models.URLField(max_length=200, null=True)

    class Meta:
        verbose_name = "Сериал"
        verbose_name_plural = "Сериалы"

    def __str__(self) -> str:
        return self.name