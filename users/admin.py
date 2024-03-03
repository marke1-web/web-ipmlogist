from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Role


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Role, RoleAdmin)


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    filter_horizontal = (
        'groups',
        'user_permissions',
        'roles',
    )


admin.site.register(User, CustomUserAdmin)
