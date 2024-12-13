#from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.filters import OrderingFilter
from .serializers import CarSerializer, BrandSerializer
from .models import Car, Brand
'''
class CarList(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

class BrandList(APIView):
    def get(self, request):
        brand = Brand.objects.all()
        serializer = BrandSerializer(brand, many=True)
        return Response(serializer.data)

class JapanBrandList(APIView):
    def get(self, request):
        brands = Brand.objects.filter(country='Japan')
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
'''
class commentaryList(APIView):
    def get(self, request):
        """TODO: Docstring for get.

        :request: TODO
        :returns: TODO

        """
        response = request.get('https://bbr.ru/graphql/')

class FilteredList(APIView):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['year']
    ordering = ['year']

    def get(self, request):
        params = request.query_params
        data_type = params.get('type')
        year_start = params.get('year_start')
        year_stop = params.get('year_stop')
        mileage_start = params.get('mileage_start')
        mileage_stop = params.get('mileage_stop')
        engine_volume_start = params.get('engine_volume_start')
        engine_volume_stop = params.get('engine_volume_stop')
        filter_conditions = {}

        if year_start:
            filter_conditions['year__gte'] = int (year_start)
        if year_stop:
            filter_conditions['year__lte'] = int (year_stop)
        if mileage_start:
            filter_conditions['mileage__gte'] = int (mileage_start)
        if mileage_stop:
            filter_conditions['mileage__lte'] = int (mileage_stop)
        if engine_volume_start:
            filter_conditions['engine_volume__gte'] = int (engine_volume_start)
        if engine_volume_stop:
            filter_conditions['engine_volume__lte'] = int (engine_volume_stop)
        if 'country' in params:
            filter_conditions['brand_country__country'] = params.get('country')
        if 'brand' in params:
            filter_conditions['brand_country__brand__icontains'] = params.get('brand')
        if 'model' in params:
            filter_conditions['model__icontains'] = params.get('model')
        if 'year' in params:
            filter_conditions['year'] = params.get('year')
        if 'mileage' in params:
            filter_conditions['mileage'] = params.get('mileage')
        if 'price' in params:
            filter_conditions['price'] = params.get('price')
        if 'transmission' in params:
            filter_conditions['transmission__icontains'] = params.get('transmission')
        if 'engine_volume' in params:
            filter_conditions['engine_volume__icontains'] = params.get('engine_volume')
        if 'drive' in params:
            filter_conditions['drive__icontains'] = params.get('drive')
        if 'color' in params:
            filter_conditions['color__icontains'] = params.get('color')
        if 'power_volume' in params:
            filter_conditions['power_volume__icontains'] = params.get('power_volume')
        ordering = self.request.query_params.get('ordering', 'id')
        
        if data_type == 'cars':
            queryset = Car.objects.all().order_by(ordering)
            if filter_conditions:
                queryset = queryset.filter(**filter_conditions)
            serializer = CarSerializer(queryset, many=True)
        elif data_type == 'brands':
            queryset = Brand.objects.all()
            if filter_conditions:
                queryset = queryset.filter(**filter_conditions)
            serializer = BrandSerializer(queryset, many=True)
        else:
            return Response({'error': 'Invalid type. Use "cars" or "brands".'}, status=400)
        
        return Response(serializer.data)


