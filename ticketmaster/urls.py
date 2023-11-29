from django.urls import path
from ticketmaster import views

urlpatterns = [
    path('', views.index, name='ticketmaster-index'),
]