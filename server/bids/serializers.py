from rest_framework import serializers
from .models import bids

class BidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bids
        fields = ['id', 'name', 'phone_number', 'description']
