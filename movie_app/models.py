from django.db import models
from django.db.models import Avg


class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    # @property
    # def movies_count(self):
    #     return 2+3


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        return self.director.name if self.director else 'No director.'

    @property
    def rating(self):
        return self.reviews.aggregate(avg_rating=Avg('stars'))['avg_rating']

    # @property
    # def movies_count(self):
    #     return sum(self.movie)


class Review(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(null=True, blank=True)

    stars = models.IntegerField(
        choices=(
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        ), default=1
    )

    def __str__(self):
        return self.movie.title

