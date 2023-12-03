from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ticketmaster-index'),
    path('register/', views.register_veiws, name='register'),
    path('login/', views.login_veiws, name='login'),
]