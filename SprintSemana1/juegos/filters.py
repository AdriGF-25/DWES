import django_filters
from .models import Juego, Consola

class JuegoFilter(django_filters.FilterSet):
    precio_min = django_filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio_max = django_filters.NumberFilter(field_name='precio', lookup_expr='lte')
    stock_min = django_filters.NumberFilter(field_name='stock', lookup_expr='gte')

    class Meta:
        model = Juego
        fields = ['consola']
