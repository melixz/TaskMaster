from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TaskMaster.settings")

app = Celery("TaskMaster")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
