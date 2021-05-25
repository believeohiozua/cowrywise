from django.contrib import admin
from .models import UuidGenerator


@admin.register(UuidGenerator)
class UuidGenerator(admin.ModelAdmin):
    list_display = ('uuid', 'timestamp')
