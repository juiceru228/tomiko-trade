from .views import getCurrencies, priceCalculation
from celery import shared_task
import json
import logging
from django.http import JsonResponse
logger = logging.getLogger('django')


@shared_task()
def update_currencies_task():
    data = getCurrencies()
    logger.info(data)
    priceCalculation()
    if isinstance(data, JsonResponse):
        data = json.loads(data.content)
    return data



