from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name = 'ingredients')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name