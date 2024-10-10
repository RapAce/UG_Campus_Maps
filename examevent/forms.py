from django import forms
from .models import ExamEvent
from django.forms import widgets,ModelForm,NumberInput

#custom widgets
class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'




class ExamEventForm(forms.ModelForm):
    class Meta:
        model=ExamEvent
        fields=[
            "coursetitle",
            "coursecode",
            "venue",
            "date",
            "starttime",
            "endtime",
            "school",
            "department",
            "college",
            "level",
        ]
        widgets = {

            'date':DateInput(),
            'starttime':TimeInput(),
            'endtime':TimeInput(),
            'level': NumberInput(attrs={'step': 100, 'min': 100,'max':600}),


        }