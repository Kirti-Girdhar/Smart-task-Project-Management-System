from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):

    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (

        ('Additional Info', {
            'fields': (
                'role',
                'phone_number',
                'profile_image',
            )
        }),

    )

    add_fieldsets = UserAdmin.add_fieldsets + (

        ('Additional Info', {
            'fields': (
                'role',
                'phone_number',
                'profile_image',
            )
        }),

    )

    list_display = (
        'username',
        'email',
        'role',
        'phone_number',
        'is_staff',
    )

admin.site.register(CustomUser, CustomUserAdmin)
