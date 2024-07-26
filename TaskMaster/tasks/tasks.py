from celery import shared_task
from time import sleep
from .models import Task


@shared_task
def process_task(task_id):
    sleep(10)
    task = Task.objects.get(id=task_id)
    task.status = "completed"
    task.save()
