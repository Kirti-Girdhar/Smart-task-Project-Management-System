from django.db import models
from organizations.models import Organization


class Workspace(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='workspaces')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'organization'], name='unique_workspace_name_per_org')
        ]
        ordering = ['name']

    def __str__(self):
        return f"{self.organization.name} - {self.name}"

