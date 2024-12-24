from django.http import JsonResponse
from json import JSONDecodeError
from datetime import datetime
import requests
from currencies.utils.redis_client import redis_client
from celery import shared_task
from decouple import config
import json
import logging

logger = logging.getLogger('django')


VK_ACCESS_TOKEN = config('VK_ACCESS_TOKEN')

CACHE_EXPIRY = 12 * 60 * 60

# Create your views here.
def getClips(request=None):
    CACHE_KEY = "vkclips_rates"
    cached_data = redis_client.get(CACHE_KEY)
    if cached_data:
        logger.info("cached")
        return JsonResponse(json.loads(cached_data))

    url = 'https://api.vk.com/method/execute'
    params = {
    "v": "5.245",
    "client_id": "6287487",
    "oauth": "2",
    "code": "return [API.shortVideo.getOwnerVideos({\"owner_id\":499628829,\"fields\":\"friend_status,is_subscribed,is_member,photo_50,photo_100,photo_200,photo_400,is_nft,about,description,followers_count,members_count,verified\",\"count\":10}),API.shortVideo.getOwnerVideos({\"owner_id\":499628829,\"playlist\":\"scheduled\",\"fields\":\"friend_status,is_subscribed,is_member,photo_50,photo_100,photo_200,photo_400,is_nft,about,description,followers_count,members_count,verified\",\"count\":10})];",
    "access_token": VK_ACCESS_TOKEN
    }
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        data = response.json()
        redis_client.set(CACHE_KEY, json.dumps(data), ex=CACHE_EXPIRY)
        logger.info("update vkclips via celery")
        return JsonResponse(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"error request to API: {e}")
        return JsonResponse({"error": "error request to API"}, status=500)
    

def getReviews(request=None):
    CACHE_KEY = "reviews_rates"
    cached_data = redis_client.get(CACHE_KEY)
    if cached_data:
        logger.info("cached")
        return JsonResponse(json.loads(cached_data))

    url = 'https://public-api.reviews.2gis.com/2.0/branches/3518965489880232/reviews'

    params = {
        'limit': 8,
        'is_advertiser': 'false',
        'fields': 'meta.providers,meta.branch_rating,meta.branch_reviews_count,meta.total_count,reviews.hiding_reason,reviews.is_verified',
        'without_my_first_review': 'false',
        'rated': 'true',
        'sort_by': 'friends',
        'key': 'b0209295-ae15-48b2-acb2-58309b333c37',
        'locale': 'ru_RU'
    }
 
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        redis_client.set(CACHE_KEY, json.dumps(data), ex=CACHE_EXPIRY)
        logger.info("update reviews via celery")
        return JsonResponse(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"error request to API: {e}")
        return JsonResponse({"error": "error request to API"}, status=500)