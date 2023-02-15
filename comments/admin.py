from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = (
        "user",
        "place",
        "relation"
        "description",
        "created_at",
    )