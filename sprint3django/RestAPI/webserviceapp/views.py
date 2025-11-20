
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Libros

#  Create your views here.

def pagina_de_prueba(request):
	return HttpResponse("<h1>Hola caracola</h1>");

def devolver_libros(request):
	lista = Libros.objects.all()
	respuesta_final = []
	for fila_sql in lista:
		diccionario = {}
		diccionario['id'] = fila_sql.id
		diccionario['nombre'] = fila_sql.nombre
		diccionario['año_publicacion'] = fila_sql.año_publicacion
		respuesta_final.append(diccionario)
	return JsonResponse (respuesta_final, safe=False)

def devolver_libros_por_id(request, id_solicitado):
        libro = Libros.objects.get(id = id_solicitado)
        comentarios = libro.comentarios_set.all()
        lista_comentarios = []
        for fila_comentario_sql in comentarios:
                diccionario = {}
                diccionario['ID'] = fila_comentario_sql.id
                diccionario['Comentario'] = fila_comentario_sql.comentario
                lista_comentarios.append(diccionario)
        resultado = {
                'id': libro.id,
                'nombre': libro.nombre,
                'año_publicacion': libro.año_publicacion,
                'comentarios': lista_comentarios
        }
        return JsonResponse(resultado, json_dumps_params={'ensure_ascii': False})
