from django.contrib import admin
from home.models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=["first_name", "last_name", "created"]

admin.site.register(Person, PersonAdmin)