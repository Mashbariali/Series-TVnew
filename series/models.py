from django.db import models
from django.utils import timezone



class Series(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    photo = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'series_series'

        verbose_name = 'series List'

class Review(models.Model):
    content = models.TextField()
    series = models.ForeignKey(Series, on_delete=models.CASCADE)


class Suggestions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)








