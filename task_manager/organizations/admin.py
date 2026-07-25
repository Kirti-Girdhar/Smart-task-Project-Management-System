from django.contrib import admin
from organizations.models import Organization

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'owner', 'created_at',)
    search_fields = ('name', 'owner__username',)
    list_filter = ('created_at',)
    ordering = ('name',)