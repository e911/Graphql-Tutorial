from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    description = models.TextField(max_length=120)
    other = models.TextField(max_length=100)

    def __str__(self):
        return self.name