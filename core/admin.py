from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["username", "email", "is_moderator"]

def get_fieldsets(self, request, obj=None):
    fieldsets = super().get_fieldsets(request, obj)
    fieldsets += (
        ("Permissions", {"fields": ("is_moderator",)}),
    )
    return fieldsets
