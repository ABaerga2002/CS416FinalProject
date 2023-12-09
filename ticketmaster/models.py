from django.db import models
from django.contrib.auth.models import User


class EventList(models.Model):
    eventName = models.CharField(max_length=100)
    eventDate = models.CharField(max_length=100)
    eventTime = models.CharField(max_length=100)
    eventURL = models.CharField(max_length=100)


# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     eventName = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=9, decimal_places=2)
#     quantity = models.IntegerField()
#     category = models.CharField(max_length=20, blank=True, choices=PRODUCT_CATEGORY)
#     image = models.ImageField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True)
#
#     def __str__(self):
#         return self.description