from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .tasks import process_task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=["post"])
    def start_processing(self, request, pk=None):
        task = self.get_object()
        if task.status == "pending":
            task.status = "in_progress"
            task.save()
            process_task.delay(task.id)
            return Response(
                {"status": "Task is being processed"}, status=status.HTTP_202_ACCEPTED
            )
        return Response(
            {"status": "Task is not in pending state"},
            status=status.HTTP_400_BAD_REQUEST,
        )
