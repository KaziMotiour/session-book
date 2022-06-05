from django.db import models
import datetime 
from django import utils

# Create your models here.
class Artist(models.Model):
    # date = models.DateField(auto_now_add=True, )
    name = models.CharField(max_length=10)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.PROTECT)