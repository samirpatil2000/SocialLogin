from .models import country
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = country
        fields = '__all__'
