from django import forms
from .models import TestAvailability

class TestAvailabilityForm(forms.ModelForm):
    class Meta:
        model = TestAvailability
        fields = '__all__'