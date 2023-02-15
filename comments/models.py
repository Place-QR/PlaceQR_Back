from django.db import models
from common.models import CommonModel


class Comment(CommonModel):
    
    """ Comment from a user to a Room or Experience"""
    
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    
    description = models.TextField(
        default="",
    )
    
    relation = models.TextField(
        default="",
    )
    
    place = models.ForeignKey(
        "places.Place",
        null=True,
        on_delete=models.SET_NULL,
        related_name="comments",
    )
    