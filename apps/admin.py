from django.contrib import admin
from .models import StreamConfig

@admin.register(StreamConfig)
class StreamConfigAdmin(admin.ModelAdmin):
    list_display = ("stream_id", "region_id", "is_active")
    list_filter = ("is_active",)
