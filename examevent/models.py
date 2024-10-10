from django.db import models
from venue.models import Venue


class ExamEvent(models.Model):
    coursetitle = models.CharField(max_length=120)
    coursecode = models.CharField(max_length=120)
    venue = models.ForeignKey(Venue, default=1, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    starttime = models.TimeField(auto_now=False, auto_now_add=False)
    endtime = models.TimeField(auto_now=False, auto_now_add=False)
    college=models.CharField(max_length=120)
    school=models.CharField(max_length=120)
    department=models.CharField(max_length=120)
    level=models.IntegerField(default=100)


    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)


    def __str__(self):
        return self.coursetitle

