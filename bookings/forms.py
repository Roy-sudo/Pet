from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['forename','surname','gender', 'description', 'date_from', 'date_until','date_booked', 'phone', 'service', 'price', 'quantity'] 