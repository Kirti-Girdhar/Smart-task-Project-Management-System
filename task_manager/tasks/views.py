import logging
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes,action
from rest_framework.permissions import IsAuthenticated
from tasks.serializers import TaskSerializer
from tasks.models import Task
from django.core.cache import cache

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

logger = logging.getLogger(__name__)

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def task_list(request):

#     if request.method == "GET":
#         task= Task.objects.all()
#         serializer= TaskSerializer(task, many= True)
#         return Response(serializer.data)

#     elif request.method== "POST":
#         serializer= TaskSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# @api_view(['GET','PUT','DELETE'])
# @permission_classes([IsAuthenticated])
# def task_detail(request, id):
#     task= get_object_or_404(Task, pk=id)
#     if task.assigned_to != request.user:
#         return Response({"message": "You are not authorized to perform this action"},
#         status=status.HTTP_403_FORBIDDEN)

#     if request.method == "GET":
#         serializer= TaskSerializer(task)
#         return Response(serializer.data)

#     elif request.method== "PUT":
#         serializer= TaskSerializer(task, data=request.data, partial= True,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     elif request.method== "DELETE":
#         task.delete()
#         return Response({"message": "Task deleted successfully"})
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter]

    filterset_fields=['status','priority']
    search_fields= ['title','description']
    ordering_fields= ['created_at','priority']

    def get_queryset(self):
        logger.info(f"Task retrieved by {self.request.user.username}")
        return Task.objects.filter(assigned_to= self.request.user).select_related('assigned_to')
    
    def perform_create(self, serializer):
        logger.info(f"Task created by user: {self.request.user.username}")
        serializer.save(assigned_to=self.request.user)
        cache.delete('my_tasks')

    @action(detail=False, methods=['GET'])
    def cached_tasks(self, request):
        cached_data= cache.get('my_tasks')
        if cached_data:
            return Response({'source':'cache', 'data':cached_data})
        tasks=self.get_queryset()
        self.serializer=self.get_serializer(tasks,many= True)
        cache.set('my_tasks', self.serializer.data,timeout=60)
        return Response({'source':'database', 'data': self.serializer.data})
    