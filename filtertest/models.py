from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=20)
    is_domesticated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

