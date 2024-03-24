from django.contrib import admin

from users.models import profile, users


@admin.register(users.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name",)


@admin.register(profile.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
