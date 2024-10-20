from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seat_choice', 'email', 'phone_number']


class SearchBusesForm(forms.Form):
    from_location = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Звідки'})
    )
    to_location = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Куди'})
    )
    departure_time = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class ProfilePhotoForm(forms.Form):
    photo = forms.ImageField(
        label="Зображення",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        error_messages={'invalid': "Тільки файли зображень (.png, .jpg, .jpeg) допускаються"}
    )

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')

        max_size = 5 * 1024 * 1024
        if photo.size > max_size:
            raise forms.ValidationError("Розмір зображення не може перевищувати 5MB.")

        return photo