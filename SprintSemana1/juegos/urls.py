from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsolaViewSet, JuegoViewSet

router = DefaultRouter()
router.register(r'consolas', ConsolaViewSet, basename='consola')
router.register(r'juegos', JuegoViewSet, basename='juego')

urlpatterns = [
    path('api/', include(router.urls)),
]
