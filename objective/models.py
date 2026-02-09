from django.contrib.auth.models import User
from django.db import models
from .models import Module


class Objective(models.Model):
    """
    Stores each Learning Objective
    """

    id = models.CharField(max_length=20, primary_key=True)
    slug = models.SlugField(max_length=20, unique=True)
    module = models.ForeignKey(Module, related_name="module_objective")
    number = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET(str(User.username)))
