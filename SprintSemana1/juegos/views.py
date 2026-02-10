from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Consola, Juego
from .serializers import ConsolaSerializer, JuegoSerializer, JuegoCreateSerializer

class ConsolaListAPIView(APIView):
    def get(self, request):
        consolas = Consola.objects.all()
        serializer = ConsolaSerializer(consolas, many=True)
        return Response(serializer.data)

class ConsolaDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            consola = Consola.objects.get(pk=pk)
            serializer = ConsolaSerializer(consola)
            return Response(serializer.data)
        except Consola.DoesNotExist:
            return Response({"error": "Consola no encontrada"}, status=404)

class JuegoListCreateAPIView(APIView):
    def get(self, request):
        juegos = Juego.objects.all()
        serializer = JuegoSerializer(juegos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JuegoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
