from django.contrib import admin
# Register your models here.
from first.models import StarWars


class FirstAdmin(admin.ModelAdmin):
    class Meta:
        model = StarWars

admin.site.register(StarWars, FirstAdmin)