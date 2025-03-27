from django.urls import path, include
from rest_framework import routers
from polls.api_views import UserViewSet, ContainerViewSet, RentalViewSet, SibTransLogViewSet, NotificationViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Роутер для API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'containers', ContainerViewSet)
router.register(r'rentals', RentalViewSet)
router.register(r'sibtranslogs', SibTransLogViewSet)
router.register(r'notifications', NotificationViewSet)

# Схема для документации
schema_view = get_schema_view(
    openapi.Info(
        title="Контейнеры API",
        default_version='v1',
        description="API для работы с контейнерами и арендой",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@containerapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include(router.urls)),  # Все маршруты для API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]