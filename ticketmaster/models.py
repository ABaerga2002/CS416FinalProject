from django.db import models
from django.contrib.auth.models import User


class EventList(models.Model):
    eventName = models.CharField(max_length=100)
    imageURL = models.CharField(max_length=100, blank=True)
    eventDate = models.CharField(max_length=100)
    eventTime = models.CharField(max_length=100)
    venueName = models.CharField(max_length=100, blank=True)
    venueCity = models.CharField(max_length=100, blank=True)
    venueState = models.CharField(max_length=100, blank=True)
    venueAdd = models.CharField(max_length=100, blank=True)
    eventURL = models.CharField(max_length=100)


class CartEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=100)
    imageURL = models.CharField(max_length=100, blank=True)
    eventDate = models.CharField(max_length=100)
    eventTime = models.CharField(max_length=100)
    venueName = models.CharField(max_length=100, blank=True)
    venueCity = models.CharField(max_length=100, blank=True)
    venueState = models.CharField(max_length=100, blank=True)
    venueAdd = models.CharField(max_length=100, blank=True)
    eventURL = models.CharField(max_length=100)

    def __str__(self):
        return ()

    