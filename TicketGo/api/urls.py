from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking_form, name='booking_form'),
    path('success/', views.success, name='success'),
    path('categories/', views.show_category, name='show_category'),
    path('transports/', views.show_all_transport, name='show_all_transport'),
    path('transports/<slug:category_id>/', views.show_transport, name='show_transport'),
]
