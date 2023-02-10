from rest_framework import serializers
from .models import Comment
from photos.serializers import PhotoSerializer
class CommentListSerializer(serializers.ModelSerializer):
      
    photos = PhotoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Comment
        
        fields = "__all__"