
from django import forms
from .models import AmbulanceRequest

class AmbulanceRequestForm(forms.ModelForm):
      class Meta:
        model = AmbulanceRequest
        fields = ['from_address', 'to_address', 'phone']
        widgets = {
            'from_address': forms.TextInput(attrs={'placeholder': 'Enter pickup address'}),
            'to_address': forms.TextInput(attrs={'placeholder': 'Enter destination address'}),
            'phone': forms.TextInput(attrs={'placeholder': '+880'}),
        }
