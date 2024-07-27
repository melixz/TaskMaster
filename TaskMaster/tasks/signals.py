from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Task
from .documents import TaskDocument


@receiver(post_save, sender=Task)
def index_task(sender, instance, **kwargs):
    task_doc = TaskDocument(
        meta={"id": instance.id},
        title=instance.title,
        description=instance.description,
        created_at=instance.created_at,
    )
    task_doc.save()


@receiver(post_delete, sender=Task)
def delete_task(sender, instance, **kwargs):
    task_doc = TaskDocument.get(id=instance.id)
    task_doc.delete()
