from django.http import JsonResponse
from json import JSONDecodeError
from datetime import datetime
import requests
from .utils.redis_client import redis_client
from celery import shared_task

import json
import logging

logger = logging.getLogger('django')


CACHE_KEY = "currency_rates"
CACHE_EXPIRY = 12 * 60 * 60
# Create your views here.
def getCurrencies(request=None):

    cached_data = redis_client.get(CACHE_KEY)
    if cached_data:
        logger.info("cached")
        return JsonResponse(json.loads(cached_data))

    url = 'https://bbr.ru/graphql/'
    headers = {
        "Content-Type": "application/json",
        "Cookie": "city_slug=moskva; city_name=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0"
    }
    body = {
        "query": "query RatesList($rateType: RateTypeEnum, $citySlug: String, $range: InputRateRange, $officeId: Int) {\n rates(\n noPagination: true\n rateType: $rateType\n citySlug: $citySlug\n officeId: $officeId\n range: $range\n ) {\n actualAt\n elements {\n id\n rateType\n fromCurrency {\n code\n }\n toCurrency {\n code\n }\n buyRate\n buyRateStatus\n sellRate\n sellRateStatus\n lot\n }\n }\n}",
        "variables": {
            "rateType": "CASH_EXCHANGE",
            "range": None
        }
    }
    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
        redis_client.set(CACHE_KEY, json.dumps(data), ex=CACHE_EXPIRY)
        logger.info("update currencies via celery")
        return JsonResponse(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"error request to API: {e}")
        return JsonResponse({"error": "error request to API"}, status=500)
def priceCalculation():
    cached_data = redis_client.get(CACHE_KEY)
    try:
        res = JsonResponse(json.loads(cached_data))
        data = json.loads(res.content) 
    except JSONDecodeError:
        return JsonResponse({'error': 'Invalid cached data format'}, status=500)
    from parking.models import Car
    cars = Car.objects.all()
    customsLimiters = [
        (0, 200, 775),
        (200, 450, 1550),
        (450, 1200, 3100),
        (1200, 2700, 8530),
        (2700, 4200, 12000),
        (4200, 5500, 15500),
        (5500, 7000, 20000),
        (7000, 8000, 23000),
        (8000, 9000, 25000),
        (9000, 10000, 27000),
        (10000, float('inf'), 30000)
    ]
    taxLimitersUpToTheThree = [
        (0, 8500, 0.54, 2.5),
        (8500, 16700, 0.48, 3.5),
        (16700, 42300, 0.48, 5.5),
        (42300, 84500, 0.48, 7.5),
        (84500, 169000, 0.48, 15),
        (169000, float('inf'), 0.48, 20)
    ]
    taxLimitersFromThreeTFive = [
        (0, 1000, 1.5),
        (1000, 1500, 1.7),
        (1500, 1800, 2.5),
        (1800, 2300, 2.7),
        (2300, 3000, 3),
        (3000, float('inf'), 3.6)
    ]
    taxLimitersMoreThanFive = [
        (0, 1000, 3),
        (1000, 1500, 3.2),
        (1500, 1800, 3.5),
        (1800, 2300, 4.8),
        (2300, 3000, 5),
        (3000, float('inf'), 5.7)
    ]
    customDuty = 0.0
    taxValue = 0.0
    fee = 0.0
    currentYear = datetime.now().year
    
    elements = data["data"]["rates"]["elements"]
    euroToRubRate = next(
        (item["buyRate"] for item in elements if item["fromCurrency"]["code"] == "EUR" and item["toCurrency"]["code"] == "RUB"),
        None
    )
    for _, car in enumerate(cars):
        for low, high, duty in customsLimiters:
            if low*1000 < car.price <= high*1000:
                customDuty = duty
                #print(customDuty)
                break
        carAge = currentYear - car.year
        if (carAge < 3):
            for low, high, percent, volume in taxLimitersUpToTheThree: 
                if (low*euroToRubRate < car.price <= high*euroToRubRate):
                    if (customDuty * percent < volume * float(car.engine_volume) * euroToRubRate):
                        taxValue = volume * float(car.engine_volume) * euroToRubRate
                    else:
                        taxValue = customDuty * percent
                    fee = 20000 * 0.17
                    #print("taxValue", taxValue, "fee",fee)
                    break
        elif (3 <= carAge <= 5):
            for low, high, volume in taxLimitersFromThreeTFive: 
                if (low < float(car.engine_volume) <= high):
                    taxValue = volume * float(car.engine_volume) * euroToRubRate
                    fee = 20000 * 0.26
                    #print("taxValue", taxValue, "fee",fee)
                    break
        elif (carAge > 5):
            for low, high, volume in taxLimitersMoreThanFive: 
                if (low < float(car.engine_volume) <= high):
                    taxValue = volume * float(car.engine_volume) * euroToRubRate
                    fee = 20000 * 0.26
                    #print("taxValue", taxValue, "fee",fee)
                    break
        #print(carAge, customDuty, taxValue, fee, euroToRubRate)
        car.duty = customDuty + taxValue + fee
            
        car.save()