from django.db import models


class EventList(models.Model):
    eventName = models.CharField(max_length=100)
    eventDate = models.CharField(max_length=100)
    eventTime = models.CharField(max_length=100)
    eventURL = models.CharField(max_length=100)
