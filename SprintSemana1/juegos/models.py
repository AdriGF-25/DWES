from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Consola(models.Model):
    # Nombre de la consola, debe ser único
    nombre = models.CharField(max_length=50, unique=True, help_text="Nombre de la consola (único)")
    # Fabricante de la consola
    fabricante = models.CharField(max_length=50, help_text="Fabricante de la consola (Nintendo, Sega, Sony...)")

    class Meta:
        verbose_name_plural = "Consolas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Desarrolladora(models.Model):
    # Nombre de la desarrolladora, debe ser único
    nombre = models.CharField(max_length=100, unique=True, help_text="Nombre de la desarrolladora (único)")
    # País de origen de la desarrolladora
    pais = models.CharField(max_length=50, help_text="País de origen de la desarrolladora")

    def __str__(self):
        return self.nombre

class PerfilUsuario(models.Model):
    # Relación 1:1 con el modelo User de Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Usuario asociado al perfil")
    # Fecha de nacimiento del usuario, opcional
    fecha_nacimiento = models.DateField(null=True, blank=True, help_text="Fecha de nacimiento del usuario (opcional)")
    # Teléfono de contacto, opcional
    telefono = models.CharField(max_length=20, blank=True, help_text="Teléfono de contacto (opcional)")
    
    # Campos de auditoría
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación del perfil")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha de última actualización del perfil")

    class Meta:
        verbose_name = "Perfil Usuario"
    
    def __str__(self):
        return self.usuario.username

class Juego(models.Model):
    class Estado(models.TextChoices):
        NUEVO = 'N', 'Nuevo'
        USADO = 'U', 'Usado'
        SELLADO = 'S', 'Sellado'
    
    # Título del juego
    titulo = models.CharField(max_length=200, help_text="Título del juego")
    # Descripción detallada del juego
    descripcion = models.TextField(help_text="Descripción detallada del juego")
    
    # Relación 1:N con Consola
    consola = models.ForeignKey(
        Consola,
        on_delete=models.SET_NULL,
        null=True,
        help_text="Consola a la que pertenece el juego"
    )
    
    # Relación 1:N con Desarrolladora
    desarrolladora = models.ForeignKey(
        Desarrolladora,
        on_delete=models.CASCADE,
        help_text="Desarrolladora del juego"
    )
    
    # Precio del juego
    precio = models.DecimalField(max_digits=6, decimal_places=2, help_text="Precio del juego")
    # Año de lanzamiento del juego
    anyo = models.IntegerField(help_text="Año de lanzamiento del juego")
    # Estado del juego físico
    estado = models.CharField(max_length=1, choices=Estado.choices, help_text="Estado del juego (Nuevo/Usado/Sellado)")
    # Indica si el juego está disponible para venta
    disponible = models.BooleanField(default=True, help_text="Indica si el juego está disponible para venta")
    # Fecha de salida original del juego
    fecha_salida = models.DateField(help_text="Fecha de salida original del juego")
    
    # Campo de auditoría
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación del registro del juego")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Juego"
    
    def __str__(self):
        return f"{self.titulo} ({self.consola})"

class Pedido(models.Model):
    # Relación 1:N con User (cliente)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Cliente que realiza el pedido")
    # Fecha automática de creación del pedido
    fecha_pedido = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora del pedido")
    # Total del pedido
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, help_text="Total del pedido")
    
    def __str__(self):
        return f"Pedido #{self.id}"

class LineaPedido(models.Model):
    # Tabla intermedia explícita
    # Relación 1:N con Pedido
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, help_text="Pedido asociado")
    # Relación 1:N con Juego
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, help_text="Juego en la línea del pedido")
    # Cantidad de unidades del juego en este pedido
    cantidad = models.IntegerField(help_text="Cantidad de unidades del juego")
    # Precio unitario al momento del pedido
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2, help_text="Precio unitario al momento del pedido")
    
    class Meta:
        # Evita que el mismo juego aparezca dos veces en el mismo pedido
        constraints = [
            models.UniqueConstraint(fields=['pedido', 'juego'], name='unique_juego_pedido')
        ]
    
    def __str__(self):
        return f"{self.cantidad}x {self.juego.titulo}"


