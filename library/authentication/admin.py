from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ('id', 'get_user_name', 'email',
                    'created_at', 'updated_at', 'last_login', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('get_user_name',)
    search_fields = ('get_user_name',)
    ordering = ['id', 'created_at', 'updated_at', 'last_login', 'role', 'is_active', 'is_staff', 'is_superuser']
    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'role'),
        })
    )

    def get_user_name(self, obj):
        return f"{obj.last_name} {obj.first_name} {obj.middle_name}"
    get_user_name.short_description = 'User Name'

    def save_model(self, request, obj, form, change):
        if not change:
            password = form.cleaned_data.get('password')
            if password:
                obj.set_password(password)
        obj.save()
