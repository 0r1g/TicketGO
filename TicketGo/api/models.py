from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Transport(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    transport_category = models.CharField(max_length=100)

    def __str__(self):
        return self.transport_category


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)

    def __str__(self):
        return self.user, self.transport
