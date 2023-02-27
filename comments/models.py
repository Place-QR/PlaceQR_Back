from django.db import models
from common.models import CommonModel


class Comment(CommonModel):
    
    """ Comment from a user to a Room or Experience"""
    
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comments",
        blank=True,
        default="None",
        null=True
    )

    name = models.TextField(null=True)
    
    relation = models.TextField(null=True)

    contact = models.TextField(null=True)

    description = models.TextField(
        default="",
    )

    photo = models.ImageField(null=True)
    
    place = models.ForeignKey(
        "places.Place",
        null=True,
        on_delete=models.SET_NULL,
        related_name="comments",
    )
    