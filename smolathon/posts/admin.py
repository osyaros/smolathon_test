from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import EventPost, CulturePost


# Register your models here.

@admin.register(EventPost)
class EventPostAdmin(admin.ModelAdmin):
    inlines = []
    search_fields = (
        'category',
        'subcategory',
        'title',
    )


@admin.register(CulturePost)
class CulturePostAdmin(admin.ModelAdmin):
    inlines = []


