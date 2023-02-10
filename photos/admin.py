from django.contrib import admin
from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "file",
        "comment",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )
    
