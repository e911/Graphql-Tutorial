from django.contrib import admin

# Register your models here.
from cookbook.models import Category, Ingredient


class SecondAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


class ThirdAdmin(admin.ModelAdmin):
    class Meta:
        model = Ingredient

admin.site.register(Category, SecondAdmin)
admin.site.register(Ingredient, ThirdAdmin)
