from django import forms
from .models import EventTyppe

class CategoryForm(forms.ModelForm):
    class Meta:
        model=EventTyppe
        fields=[
            "type"

        ]