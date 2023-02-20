from rest_framework import serializers
from .models import Place
from comments.models import Comment
from photos.serializers import PhotoSerializer

class PlaceListSerializer(serializers.ModelSerializer):
    
    # photo = PhotoSerializer(read_only=True)
    # is_owner = serializers.SerializerMethodField()
    class Meta:
        model = Place
        
        fields = (
            "pk",
            "name",
            "owner",
            "description",
            "address",
            "photo",
        )
        
    def get_is_owner(self, place):
        request = self.context["request"]
        return place.owner == request.user
    
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class PlaceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"