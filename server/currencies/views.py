from django.http import JsonResponse
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
