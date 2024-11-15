from rest_framework import serializers
from .models import Travel, UTravel

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'

class UTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UTravel
        fields = '__all__'