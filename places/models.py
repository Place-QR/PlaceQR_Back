from django.db import models
from common.models import CommonModel

class Place(CommonModel):
    
    """Place Model Definition"""
    
    name = models.CharField(
        max_length=180,
        default="",
    )
    description = models.TextField()
    address = models.CharField(max_length=250,)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="places",
    )
    photo = models.ImageField(null=True)
    
    def __str__(self) -> str:
        return self.name
