from rest_framework.viewsets import ModelViewSet
from .models import Consola, Juego
from .serializers import ConsolaSerializer, JuegoSerializer, JuegoCreateSerializer

class ConsolaViewSet(ModelViewSet):
    queryset = Consola.objects.all()
    serializer_class = ConsolaSerializer

class JuegoViewSet(ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return JuegoCreateSerializer
        return JuegoSerializer
