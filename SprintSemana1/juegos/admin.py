from django.contrib import admin
from .models import Consola, Desarrolladora, PerfilUsuario, Juego, Pedido, LineaPedido

# Register your models here.

admin.site.register(Consola)
admin.site.register(Desarrolladora)
admin.site.register(PerfilUsuario)

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'consola', 'desarrolladora', 'precio', 'estado', 'disponible')
    list_filter = ('consola', 'desarrolladora', 'estado', 'disponible')
    search_fields = ('titulo', 'descripcion')
    
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'total', 'fecha_pedido')
    list_filter = ('fecha_pedido',)
    search_fields = ('cliente__username',)

@admin.register(LineaPedido)
class LineaPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'juego', 'cantidad', 'precio_unitario')
    list_editable = ('cantidad', 'precio_unitario')
    list_filter = ('pedido',)

