from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ticketmaster-index'),
    path('register/', views.register_veiws, name='register'),
    path('login/', views.login_veiws, name='login'),
    path('logout/', views.logout_veiws, name='logout'),
    path('cart/', views.view_cart, name='cart'),
    path('addCart/<int:event_id>/', views.add_cart, name='add'),
    path('remove/<int:event_id>/', views.remove_cart, name='remove')
]
