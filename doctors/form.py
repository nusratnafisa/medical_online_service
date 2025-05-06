from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
   class Meta:
    model = Doctor
    fields = '__all__'  # ✅ This is actually correct if it's exactly like this
widgets = {
            'hospitals': forms.SelectMultiple(attrs={'class': 'select2'}),
            'dept_names': forms.SelectMultiple(attrs={'class': 'select2'}),
    }