from django.urls import path
from . import views
from .views import PlacePhoto

urlpatterns = [
    path("", views.PlaceList.as_view()),
    path("<int:pk>", views.PlaceDetail.as_view()),
    path("<int:pk>/photo", PlacePhoto.as_view()),
]