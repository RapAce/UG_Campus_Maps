from django.db import models


class EventTyppe(models.Model):
    type=models.CharField(max_length=120)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.type