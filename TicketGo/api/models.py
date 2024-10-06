from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Bus(models.Model):
    class Choices(models.TextChoices):
        NO = 'No', 'Not Available'
        YES = 'Yes', 'Available'

    company_name = models.ForeignKey('Company', on_delete=models.CASCADE)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()
    wi_fi_availability = models.CharField(max_length=3, choices=Choices.choices)
    socket_availability = models.CharField(max_length=3, choices=Choices.choices)
    toilets_available = models.CharField(max_length=3, choices=Choices.choices, null=True)
    conditioner_available = models.CharField(max_length=3, choices=Choices.choices, null=True)

    class Meta:
        verbose_name_plural = 'Buses'

    def trip_duration(self):
        return self.arrival_time - self.departure_time

    def __str__(self):
        return f'{self.company_name}, {self.from_location} -> {self.to_location}'


class Company(models.Model):
    name = models.CharField(max_length=100)
    official_name = models.CharField(max_length=100)
    registered_address = models.TextField()
    company_registration_number = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Booking(models.Model):
    class SeatChoice(models.TextChoices):
        ECK = 'EC', 'Economy Class'
        LK = 'LK', 'Luxury Class'
        BK = 'BK', 'Business Class'
        VIP = 'VP', 'VIP Class'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_choice = models.CharField(max_length=2, choices=SeatChoice.choices)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )

    class Meta:
        verbose_name_plural = 'Booking'

    def __str__(self):
        return f'{self.user}, {self.bus}'


# class UploadFiles(models.Model):
#     file = models.FileField(upload_to='uploads_model')
#
#     class Meta:
#         verbose_name_plural = 'Upload Files'


class ProfilePhoto(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
