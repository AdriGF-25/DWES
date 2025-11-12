class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def mostrar_info(self):
        estado = "Completada" if self.completada else "Pendiente"
        return "Título: " + self.titulo + " | Estado: " + estado

    def marcar_completada(self):
        self.completada = True

    def editar(self, nuevo_titulo, nueva_descripcion):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion

def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            crear_tarea(tareas)
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            editar_tarea(tareas)
        elif opcion == "5":
            eliminar_tarea(tareas)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Crear tarea")
    print("2. Mostrar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Editar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")


def crear_tarea(tareas):
    titulo = input("Título de la tarea: ").strip()
    descripcion = input("Descripción de la tarea: ").strip()
    nueva_tarea = Tarea(titulo, descripcion)
    tareas.append(nueva_tarea)
    print("Tarea creada correctamente.")


def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, start=1):
            print(str(i) + ". " + tarea.mostrar_info())


def marcar_completada(tareas):
    titulo = input("Introduce el título de la tarea a completar: ").strip().lower()
    for tarea in tareas:
        if tarea.titulo.lower() == titulo:
            tarea.marcar_completada()
            print("Tarea marcada como completada.")
            return
    print("No se encontró ninguna tarea con ese título.")


def editar_tarea(tareas):
    titulo = input("Introduce el título de la tarea a editar: ").strip().lower()
    for tarea in tareas:
        if tarea.titulo.lower() == titulo:
            nuevo_titulo = input("Nuevo título: ").strip()
            nueva_descripcion = input("Nueva descripción: ").strip()
            tarea.editar(nuevo_titulo, nueva_descripcion)
            print("Tarea editada correctamente.")
            return
    print("No se encontró ninguna tarea con ese título.")


def eliminar_tarea(tareas):
    titulo = input("Introduce el título de la tarea a eliminar: ").strip().lower()
    for tarea in tareas:
        if tarea.titulo.lower() == titulo:
            tareas.remove(tarea)
            print("Tarea eliminada correctamente.")
            return
    print("No se encontró ninguna tarea con ese título.")



if __name__ == "__main__":
    main()