from django.contrib import admin

from home.models import Address, Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=["first_name", "last_name", "created"]

class AddressAdmin(admin.ModelAdmin):
    list_display=["street", "city", "province"]

admin.site.register(Person, PersonAdmin)
admin.site.register(Address, AddressAdmin)