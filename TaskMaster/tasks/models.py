from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .documents import TaskDocument


class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "В очереди"),
        ("in_progress", "В процессе"),
        ("completed", "Завершена"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Task)
def index_task(sender, instance, **kwargs):
    task_doc = TaskDocument(
        meta={"id": instance.id},
        title=instance.title,
        description=instance.description,
        created_at=instance.created_at,
    )
    task_doc.save()
