from django.contrib import admin
from .models import Place


@admin.register(Place)
class RoomAdmin(admin.ModelAdmin):
    
    list_display = (
        "name",
        "description",
        "created_at",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )
    
    search_fields = (
        "name",
        # "owner__username"
    )


# @admin.register(Photo)
# class PhotoAdmin(admin.ModelAdmin):
#     pass
