from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from tasks.serializers import TestSerializer
from tasks.models import Task

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def task_list(request):

    if request.method == "GET":
        task= Task.objects.all()
        serializer= TestSerializer(task, many= True)
        return Response(serializer.data)

    elif request.method== "POST":
        serializer= TestSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def task_detail(request, id):
    task= get_object_or_404(Task, pk=id)
    if task.assigned_to != request.user:
        return Response({"message": "You are not authorized to perform this action"},
        status=status.HTTP_403_FORBIDDEN)

    if request.method == "GET":
        serializer= TestSerializer(task)
        return Response(serializer.data)

    elif request.method== "PUT":
        serializer= TestSerializer(task, data=request.data, partial= True,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method== "DELETE":
        task.delete()
        return Response({"message": "Task deleted successfully"})