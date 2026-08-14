from rest_framework import serializers
from .models import Workspace

class WorkspaceSerializer(serializers.ModelSerializer):
    organization_name = serializers.ReadOnlyField(source='organization.name')

    class Meta:
        model = Workspace
        fields = ['id', 'name', 'organization', 'organization_name', 'created_at', 'updated_at']

        read_only_fields = ['organization_name', 'organization', 'created_at', 'updated_at']