from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('companies/', views.show_companies, name='show_companies'),
    path('companies/<int:company_id>/', views.show_company_details, name='show_company_details'),
    path('buses/', views.show_buses, name='show_buses'),
    path('buses/<int:bus_id>/', views.show_bus, name='show_buses'),
    path('booking/show/<int:booking_id>/', views.view_booking, name='view_booking'),
    path('booking/<int:bus_id>/', views.booking_form, name='booking_form'),
    path('success/<int:booking_id>/', views.success, name='success'),
    path('me/', views.profile, name='profile'),
]
