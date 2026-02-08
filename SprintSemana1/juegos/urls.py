from django.urls import path
from .views import ConsolaListAPIView, ConsolaDetailAPIView

urlpatterns = [
    path('api/consolas/', ConsolaListAPIView.as_view(), name='consola-list'),
    path('api/consolas/<int:pk>/', ConsolaDetailAPIView.as_view(), name='consola-detail'),
]
