from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskSearchView

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)
router.register(r"search", TaskSearchView, basename="task-search")

urlpatterns = [
    path("", include(router.urls)),
]
