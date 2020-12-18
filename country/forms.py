from django import forms
from .models import country

class countryForm(forms.ModelForm):
    class Meta:

        model = country
        fields = '__all__'