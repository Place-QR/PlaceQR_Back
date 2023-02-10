from django.db import models
from common.models import CommonModel

class Photo(CommonModel):
    
    file = models.ImageField(null=True)
    
    comment = models.ForeignKey(
        "comments.Comment",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    
    def __str__(self):
        return "Photo File"
    