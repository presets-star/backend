from django.contrib import admin

from users.models import profile


@admin.register(profile.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
