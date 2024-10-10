from django import forms
from .models import Event
from django.forms import widgets

#custom widgets
class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=[
            "name",
            "venue",
            "description",
            "startdate",
            "enddate",
            "starttime",
            "endtime",
            "type",
        ]
        widgets = {
            'startdate': DateInput(),
            'enddate':DateInput(),
            'starttime':TimeInput(),
            'endtime':TimeInput(),
        }