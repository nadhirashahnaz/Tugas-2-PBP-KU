from django.db import models

class myWatchList(models.Model):
    watched = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    release_date = models.CharField(max_length=30)
    review = models.TextField()
