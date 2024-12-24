import os

from django.conf import settings
from currencies.tasks import update_currencies_task
from others.tasks import update_others_task
#from parking.tasks import populate_db_images
from celery import Celery, signals
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tomiko_trade.settings')
import django
django.setup()
app = Celery('tomiko_trade')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.event_serializer = 'pickle' # this event_serializer is optional. 
app.conf.task_serializer = 'pickle'
app.conf.result_serializer = 'pickle'
app.conf.accept_content = ['application/json', 'application/x-python-serialize']
# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@signals.worker_ready.connect
def at_start(sender, **kwargs):
    print("Starting initial task...")
    from parking.tasks import populate_db_images
    populate_db_images.apply_async()
    update_currencies_task.apply_async()
    update_others_task.apply_async()

