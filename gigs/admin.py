from django.contrib import admin
from .models import Gig

@admin.register(Gig)
class GigAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "posted_at")
    search_fields = ("title", "company", "location")
    list_filter = ("company", "location")
    ordering = ("-posted_at",)
