from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from comments.models import Comment
from comments.serializers import CommentSerializer
from tasks.models import Task


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_comment(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(author=request.user, task=task)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    queryset = Comment.objects.select_related('author', 'task')

    def get_queryset(self):
        return Comment.objects.select_related('author', 'task')

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, 
            )
        