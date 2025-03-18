from django.db import models

# Create your models here.

class Address(models.Model):


class Person(models.Model):
    sin = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    birthday = models.DateField(null=True, blank=True)


    """_summary_

    street = ...
    province = ...
    postal_code = ...

    """

    # Created timestamp
    created = models.DateTimeField(auto_now_add=True)
    # Updated timestamp
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
