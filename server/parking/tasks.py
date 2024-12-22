from celery import shared_task
import logging
import os
from parking.models import Car

logger = logging.getLogger('django')

@shared_task
def populate_db_images():
    image_folder = 'media/cars/'
    image_files = os.listdir(image_folder)

    cars = Car.objects.all()

    for car in cars:
        image_indices = [car.id % len(image_files), (car.id + 1) % len(image_files), (car.id + 2) % len(image_files)]

        image_paths = [os.path.join('cars', image_files[i]) for i in image_indices]

        car.image = ','.join(image_paths)
        car.save()