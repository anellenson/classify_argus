from __future__ import unicode_literals
from django.db import models
from django.utils.functional import cached_property
from django.contrib.auth.models import User


class Image(models.Model): #Just the actual image
    filename = models.CharField(max_length = 1000)

    def __str__(self):
        return self.filename



class State(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self): #Play with this and see how this helps
        return self.name

class User_states_image(models.Model): #Users will be creating/updating this model
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    state = models.ForeignKey(State, on_delete = models.CASCADE)




# Create your models here.
