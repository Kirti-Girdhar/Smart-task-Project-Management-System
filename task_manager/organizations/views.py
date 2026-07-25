from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from organizations.models import Organization
from organizations.serializers import OrganizationSerializer

class OrganizationViewSet(ModelViewSet):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Organization.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)