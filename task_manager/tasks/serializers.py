from rest_framework import serializers
from tasks.models import Task
from users.models import CustomUser

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields= ['assigned_to']

    def create(self, validated_data):
        request= self.context.get('request')
        user= request.user if request else None
        # user= CustomUser.objects.first()

        task= Task.objects.create(
            assigned_to= user,
            **validated_data
        )
        return task
        