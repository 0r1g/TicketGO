from django.contrib import admin
from .models import Bus, CompanyName, Booking

# Register your models here.


@admin.register(CompanyName)
class CompanyNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'official_name', 'registered_address', 'company_registration_number')
    list_display_links = ('id', 'name')
    ordering = ['id']


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'from_location', 'to_location', 'departure_time', 'arrival_time', 'price')
    ordering = ['id']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'bus', 'user', 'seat_choice', 'email', 'phone_number')
    ordering = ['id']
