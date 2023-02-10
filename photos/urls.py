from django.urls import path, include
from .views import PhotoVeiwSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', PhotoVeiwSet)


urlpatterns = [
    path("", include(router.urls)),
]