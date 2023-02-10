from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import serializers
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    PermissionDenied,
    NotAuthenticated,
)
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Comment
from .serializers import CommentListSerializer
from photos.serializers import PhotoSerializer
from drf_yasg.utils       import swagger_auto_schema
from drf_yasg             import openapi  

class CommentList(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_comments = Comment.objects.all()
        serializer = serializers.CommentListSerializer(
            all_comments,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.CommentListSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            return Response(CommentListSerializer(comment).data)
        else:
            return Response(serializer.errors)
        
        
class CommentDetail(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    comment_id = openapi.Parameter('comment_id', openapi.IN_PATH, description='comment_id path', required=True, type=openapi.TYPE_NUMBER)

    @swagger_auto_schema(tags=['지정한 데이터의 상세 정보를 불러옵니다.'], manual_parameters=[comment_id], responses={200: 'Success'})
    
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise NotFound
        
    def get(self, request, pk):
        comment = self.get_object(pk)
        
        serializer = serializers.CommentListSerializer(
            comment,
            context={"request": request},
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        comment = self.get_object(pk)
        
        if comment.user != request.user:
            raise PermissionDenied
        
        serializer = serializers.CommentListSerializer(
            comment,
            data = request.data,
            partial = True,
        )
        
        if serializer.is_valid():
            comment = serializer.save()
            return Response(CommentListSerializer(comment).data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        comment = self.get_object(pk)
        
        if comment.user != request.user:
            raise PermissionDenied
        comment.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
class CommentPhotos(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        comment = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if request.user != comment.owner:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(comment=comment)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)