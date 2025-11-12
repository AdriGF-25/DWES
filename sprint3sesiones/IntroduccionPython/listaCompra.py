def main():
    lista_compra = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            añadir_producto(lista_compra)
        elif opcion == "2":
            eliminar_producto(lista_compra)
        elif opcion == "3":
            ver_lista(lista_compra)
        elif opcion == "4":
            vaciar_lista(lista_compra)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

def mostrar_menu():
    print("\n--- LISTA DE LA COMPRA ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Ver lista")
    print("4. Vaciar lista")
    print("5. Salir")

def añadir_producto(lista_compra):
    producto = input("Introduce el nombre del producto: ").strip().lower()
    if producto in lista_compra:
        print("Ese producto ya está en la lita.")
    else:
        lista_compra.append(producto)
        print("Producto añadido correctamente.")

def eliminar_producto(lista_compra):
    producto = input("Introduce el producto a eliminar: ").strip().lower()
    if producto in lista_compra:
        lista_compra.remove(producto)
        print("Producto eliminado.")
    else:
        print("El producto no está en la lista.")

def ver_lista(lista_compra):
    if not lista_compra:
        print("La lista está vacía.")
    else:
        print("\nLista de la compra (ordenada):")
        for producto in sorted(lista_compra):
            print("- " + producto)

def vaciar_lista(lista_compra):
    confirmacion = input("¿Seguro que quieres vaciar la lista? (s/n): ").lower()
    if confirmacion == "s":
        lista_compra.clear()
        print("Lista vaciada.")
    else:
        print("Operación cancelada.")



if __name__ == "__main__":
    main()