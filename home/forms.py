from django import forms
from home.models.address import Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = []

    def is_valid(self):
        is_valid =  super().is_valid()

        if self.cleaned_data.get("country") != "Canada":
            return False