from django.contrib import admin

# Register your models here.
from filtertest.models import Animal


class FourthAdmin(admin.ModelAdmin):
    class Meta:
        model = Animal

admin.site.register(Animal, FourthAdmin)
