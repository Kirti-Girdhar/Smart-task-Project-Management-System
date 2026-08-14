from django.contrib import admin

from .models import Workspace

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'organization', 'created_at', 'updated_at')
    search_fields = ('name', 'organization__name')
    list_filter = ('organization', 'created_at')
    ordering = ('name', 'organization')