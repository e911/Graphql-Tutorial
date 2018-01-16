from django.db import models


# Create your models here.
class StarWars(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    roll_no = models.IntegerField(default=2)

    def __str__(self):
        return self.name