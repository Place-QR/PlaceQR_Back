from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from . import serializers
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    PermissionDenied,
    NotAuthenticated,
)

from .models import Place
from .serializers import PlaceListSerializer, PhotoSerializer

import qrcode

url = "https://qrplace.loca.lt//"
file_route = "C://Users//j3hea//OneDrive//바탕 화면//Data//asdf//BE_PlaceQR//uploads//" 


class PlaceList(APIView):
    
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_places = Place.objects.all()
        serializer = serializers.PlaceListSerializer(
            all_places,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.PlaceListSerializer(data=request.data)

        # place 이미지 주소 db에 저장
        if serializer.is_valid():
            place = serializer.save()
            
            
            img = qrcode.make(url + "api/v1/places/" + str(PlaceListSerializer(place).data["pk"]))
            img.save(file_route + "qr" + str(PlaceListSerializer(place).data["pk"]) + ".png")
            
            case = Place.objects.get(pk=PlaceListSerializer(place).data["pk"])
            case.qr_img = file_route + "qr" + str(PlaceListSerializer(place).data["pk"]) + ".png"
            case.save()
            return Response(PlaceListSerializer(place).data)

        else:
            return Response(serializer.errors)
        

class PlaceDetail(APIView):
    
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_object(self, pk):
        try:
            return Place.objects.get(pk=pk)
        except Place.DoesNotExist:
            raise NotFound
        
    def get(self, request, pk):
        place = self.get_object(pk)
        
        # 데이터를 보내기 위한 serializer
        serializer = serializers.PlaceListSerializer(
            place,
            context={"request": request},
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        place = self.get_object(pk)
        
        # 방의 주인이 아닐 경우 또한 place를 수정할 수 없음
        if place.owner != request.user:
            raise PermissionDenied
        
        serializer = serializers.PlaceListSerializer(
            place,
            data = request.data,
            partial = True,
        )
        
        if serializer.is_valid():
            place = serializer.save()
            return Response(PlaceListSerializer(place).data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        place = self.get_object(pk)
        
        # 방의 주인이 아닐 경우 또한 room을 삭제할 수 없음
        if place.owner != request.user:
            raise PermissionDenied
        place.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
  
  
class PlacePhoto(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Place.objects.get(pk=pk)
        except Place.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        place = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if request.user != place.owner:
            raise PermissionDenied
        serializer = PlaceListSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(place=place)
            serializer = PlaceListSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
