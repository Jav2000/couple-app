from django import forms

from .models import Site

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'description', 'start_date', 'end_date', 'latitude', 'longitude']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'latitude': forms.TextInput(attrs={'readonly': 'readonly'}),
            'longitude': forms.TextInput(attrs={'readonly': 'readonly'}),
        }