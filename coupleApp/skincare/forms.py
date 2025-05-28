from django import forms

from .models import SkincareProduct

class SkincareProductForm(forms.ModelForm):
    class Meta:
        model = SkincareProduct
        fields = ['name', 'description', 'owned', 'brand', 'category', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el nombre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una descripción'}),
            'owned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la marca'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'placeholder': 'Escribe el precio'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)