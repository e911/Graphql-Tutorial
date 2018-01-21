from django.contrib import admin
# Register your models here.
from mutationtest.models import Person


class SixthAdmin(admin.ModelAdmin):
    class Meta:
        model = Person

admin.site.register(Person, SixthAdmin)