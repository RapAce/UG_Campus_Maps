from django import forms
from .models import Venue
from django.forms import widgets

class HiddenInput(forms.HiddenInput):
    input_type = 'hidden'

class VenueForm(forms.ModelForm):
    class Meta:
        model=Venue
        fields=[
            "name",
            "category",
            "address",
            "latitude",
            "longitude",
            "phonenumber",
            "openinghours",
            "type",
            "imageurl",
            "indoormap",

        ]
        widgets = {
        'imageurl':HiddenInput(),
        }