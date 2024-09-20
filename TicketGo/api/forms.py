from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'transport', 'type_place']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }

