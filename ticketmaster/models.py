from django.db import models


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
    eventName = models.CharField(max_length=100)
    imageURL = models.CharField(max_length=100, blank=True)
    eventDate = models.CharField(max_length=100)
    eventTime = models.CharField(max_length=100)
    venueName = models.CharField(max_length=100, blank=True)
    venueCity = models.CharField(max_length=100, blank=True)
    venueState = models.CharField(max_length=100, blank=True)
    venueAdd = models.CharField(max_length=100, blank=True)
    eventURL = models.CharField(max_length=100)