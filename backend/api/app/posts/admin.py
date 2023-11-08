from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import EventPost, CulturePost


# Register your models here.

@admin.register(EventPost)
class EventPostAdmin(admin.ModelAdmin):
    inlines = []


@admin.register(CulturePost)
class CulturePostAdmin(admin.ModelAdmin):
    inlines = []


