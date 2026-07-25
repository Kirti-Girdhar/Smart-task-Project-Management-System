from rest_framework import serializers

from organizations.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Organization
        fields = ['id', 'name', 'owner', 'description', 'created_at', 'updated_at']
        
        read_only_fields = ['owner', 'created_at', 'updated_at']