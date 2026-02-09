from django.contrib.auth.models import User
from django.db import models


class Module(models.Model):
    """
    Stores each Module
    """

    id = models.CharField(max_length=20, primary_key=True)
    slug = models.SlugField(max_length=20, unique=True)
    number = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET(str(User.username)))
