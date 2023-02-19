from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
# router.register("", PlaceViewset)



urlpatterns = [

    path("", include(router.urls)),
    # path("", views.PlaceList.as_view()),
    # path("<int:pk>", views.PlaceDetail.as_view()),
    # path("<int:pk>/photo", PlacePhoto.as_view()),
]