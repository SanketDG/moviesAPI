from django.db import models


class Genre(models.Model):
    """Genre Model for storing a Genre string"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Movie(models.Model):
    """Movies model to store a Movie object"""

    name = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)
    director = models.CharField(max_length=200)
    imdb_score = models.FloatField()
    popularity = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.director} - {self.imdb_score}"
