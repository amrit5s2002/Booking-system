from django.forms import ModelForm
from .models import *

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ['left']