from __future__ import unicode_literals
from django.db import models
from django.utils.functional import cached_property
from django.contrib.auth.models import User


class Image(models.Model): #Just the actual image
    filename = models.CharField(max_length = 1000)


class Tally(models.Model):
    total_tally = models.IntegerField(default = 0)

    def __str__(self):
        return '{}'.format(self.total_tally)

class Voter(User): #Use openDjango
    tally = models.ForeignKey(Tally, on_delete = models.CASCADE) #They need to each have a tally associated with them
    images = models.ForeignKey(Image, on_delete = models.CASCADE) #They need to be associated with images they've voted on

class State(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self): #Play with this and see how this helps
        return self.name

class User_states_image(models.Model): #Users will be creating/updating this model
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    user = models.ForeignKey(Voter, on_delete = models.CASCADE)
    state = models.ForeignKey(State, on_delete = models.CASCADE)

# Create your models here.
