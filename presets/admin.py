from django.contrib import admin

from presets.models import presets


@admin.register(presets.Preset)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "seller_id",)
