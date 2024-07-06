# crudapp/forms.py
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'dob', 'reason', 'appointment_date', 'time']
        widgets = {
            'dob': forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY'}),
            'appointment_date': forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY'}),
            'time': forms.TimeInput(attrs={'placeholder': 'HH:MM'}),
        }
