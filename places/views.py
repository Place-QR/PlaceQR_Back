from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from . import serializers
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    PermissionDenied,
    NotAuthenticated,
)
# from rest_framework import viewsets

from .models import Place
from comments.models import Comment
from .serializers import *


import qrcode
import os


url = "https://www.placeqr.store/"
file_route = str(os.getcwd()).replace("\\", "/") + "/uploads/qr/"


class PlaceViewset(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()


    def create(self, request, *args, **kwrgs):
        os.makedirs(str(os.getcwd()).replace("\\", "//") + "//uploads//qr", exist_ok=True)

        
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            place = serializer.save()
            img = qrcode.make(url + "places/" + str(PlaceSerializer(place).data["id"]))
            img.save(file_route + "qr" + str(PlaceSerializer(place).data["id"]) + ".png")
            
            case = Place.objects.get(pk=PlaceSerializer(place).data["id"])
            case.qr_img = file_route + "qr" + str(PlaceSerializer(place).data["id"]) + ".png"
            case.save()

            return Response(PlaceSerializer(place).data)

        else:
            return Response(serializer.errors)


class PlaceCommentsVeiwset(APIView):
    def get(self, request, pk):
        serializer = PlaceCommentSerializer(Comment.objects.filter(place=pk), many=True)
        return Response(serializer.data)


    





    
