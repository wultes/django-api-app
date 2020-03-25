from django.db import models
from django.utils.crypto import get_random_string

class App(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    api_key = models.CharField(max_length=40, default=get_random_string)
    version = models.CharField(max_length=40, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.name
