from django.db import models

# Create your models here.

class Stats(models.Model):
    name = 'hello'
    def __str__(self):
        return self.name
