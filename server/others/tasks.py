from .views import getClips, getReviews
from celery import shared_task
import json
import logging
from django.http import JsonResponse
logger = logging.getLogger('django')


@shared_task()
def update_others_task():
    getClips()
    getReviews()



