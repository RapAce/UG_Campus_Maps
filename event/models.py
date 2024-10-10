from django.db import models
from venue.models import Venue
from type.models import EventTyppe


class Event(models.Model):
    name = models.CharField(max_length=120)
    venue = models.ForeignKey(Venue, default=1,on_delete=models.CASCADE)
    description = models.TextField()
    startdate = models.DateField(auto_now=False, auto_now_add=False)
    enddate = models.DateField(auto_now=False, auto_now_add=False)
    starttime = models.TimeField(auto_now=False, auto_now_add=False)
    endtime = models.TimeField(auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    type = models.ForeignKey(EventTyppe, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

