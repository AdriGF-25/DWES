from django.urls import path
from .views import ConsolaListAPIView, ConsolaDetailAPIView, JuegoListCreateAPIView

urlpatterns = [
    path('api/consolas/', ConsolaListAPIView.as_view(), name='consola-list'),
    path('api/consolas/<int:pk>/', ConsolaDetailAPIView.as_view(), name='consola-detail'),
    path('api/juegos/', JuegoListCreateAPIView.as_view(), name='juego-list'),
]
