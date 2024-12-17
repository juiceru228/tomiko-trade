from celery import shared_task
import logging
logger = logging.getLogger('django')
from parking.models import Car
import os


@shared_task()
def populate_db_images():
    image_folder = 'media/cars/'
    image_files = os.listdir(image_folder)

    cars = Car.objects.all()

    for index, car in enumerate(cars):
        image_index = car.id % len(image_files)
        image_path = os.path.join('cars', image_files[image_index])

        car.image = image_path
        car.save()
populate_db_images.apply_async(countdown=0)