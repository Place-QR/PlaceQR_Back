from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="PlaceQR",
        default_version="1.1.1",
        description="PlaceQR API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=""), # 부가정보
        license=openapi.License(name="mit"),     # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

urlpatterns = [
    
    # app url
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("places/", include("places.urls")),
    path("comments/", include("comments.urls")),
    path("users/", include("users.urls")),
    path("photos/", include("photos.urls")),

    # swagger url
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
