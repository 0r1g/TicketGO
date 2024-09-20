from django.contrib import admin
from .models import Category, Transport, Booking

# Register your models here.

admin.site.register(Category)
admin.site.register(Transport)
admin.site.register(Booking)
