from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Consola
from .serializers import ConsolaSerializer

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
