from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Consola, Juego
from .serializers import ConsolaSerializer, JuegoSerializer, JuegoCreateSerializer
from .filters import JuegoFilter


class ConsolaViewSet(ModelViewSet):
    queryset = Consola.objects.all()
    serializer_class = ConsolaSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["nombre", "fabricante"]
    ordering_fields = ["id", "nombre", "fabricante"]
    ordering = ["id"]


class JuegoViewSet(ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = JuegoFilter
    search_fields = ["titulo", "descripcion"]
    ordering_fields = ["id", "titulo", "precio", "stock", "anyo", "fecha_salida"]
    ordering = ["id"]

    def get_serializer_class(self):
        if self.action == "create":
            return JuegoCreateSerializer
        return JuegoSerializer
