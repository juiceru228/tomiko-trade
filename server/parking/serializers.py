from rest_framework import serializers
from .models import Brand, Car

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'country', 'brand']

class CarSerializer(serializers.ModelSerializer):
    brand_country = BrandSerializer()

    class Meta:
        model = Car
        fields = ['id', 'model', 'year', 'mileage', 'price', 'transmission', 'engine_volume', 'drive', 'color', 'power_volume', 'image', 'duty', 'brand_country']
class CarValuesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    model = serializers.CharField()
    brand = serializers.CharField(source='brand_country.brand')
