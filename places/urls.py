from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", PlaceViewset)



urlpatterns = [
    
    path("", include(router.urls)),
    path("<int:pk>/comments/", PlaceCommentsViewset.as_view()),
    path("<int:pk>/comments/counts", PlaceCommentsCountsViewset.as_view()),
]