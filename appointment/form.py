from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'age', 'gender', 'birth_date', 'contact_info', 'appointment_date']

        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }