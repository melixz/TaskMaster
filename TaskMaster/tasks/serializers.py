from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("created_at",)

    def validate_title(self, value):
        if len(value) < 50:
            raise serializers.ValidationError(
                "Title must be at least 50 characters long."
            )
        return value

    def validate_description(self, value):
        if len(value) < 100:
            raise serializers.ValidationError(
                "Description must be at least 100 characters long."
            )
        return value
