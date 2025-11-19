# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comentarios(models.Model):
    comentario = models.CharField(max_length=2000, blank=True, null=True)
    libro = models.ForeignKey('Libros', models.DO_NOTHING)
    usuario_id = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comentarios'


class Juegos(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    url_imagen = models.CharField(max_length=200, blank=True, null=True)
    plataforma = models.CharField(max_length=50, blank=True, null=True)
    fecha_lanzamiento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'juegos'


class Libros(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    url_imagen = models.CharField(max_length=200, blank=True, null=True)
    autor = models.CharField(max_length=100, blank=True, null=True)
    año_publicacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libros'


class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'usuarios'
