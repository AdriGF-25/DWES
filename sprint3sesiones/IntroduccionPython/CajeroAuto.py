def main():
    cuenta = {"nombre": "Ana", "saldo": 1200.0}
    print(f"Bienvenida/o {cuenta['nombre']}")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            consultar_saldo(cuenta)
        elif opcion == "2":
            ingresar_dinero(cuenta)
        elif opcion == "3":
            retirar_dinero(cuenta)
        elif opcion == "4":
            print("Hasta pronto.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def consultar_saldo(cuenta):
    print(f"\n Saldo actual: {cuenta['saldo']} €")


def ingresar_dinero(cuenta):
    try:
        cantidad = float(input("¿Cuánto dinero deseas ingresar? "))
        if cantidad > 0:
            cuenta["saldo"] += cantidad
            print(f"Has ingresado {cantidad} €. Nuevo saldo: {cuenta['saldo']} €")
        else:
            print("La cantidad debe ser positiva.")
    except ValueError:
        print("Debes introducir un número válido.")


def retirar_dinero(cuenta):
    try:
        cantidad = float(input("¿Cuánto dinero deseas retirar? "))
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
        elif cantidad > cuenta["saldo"]:
            print("Saldo insuficiente.")
        else:
            cuenta["saldo"] -= cantidad
            print(f"Has retirado {cantidad:.2f} €. Nuevo saldo: {cuenta['saldo']:.2f} €")
    except ValueError:
        print("Debes introducir un número válido.")


def mostrar_menu():
    print("\n===== CAJERO AUTOMÁTICO =====")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")




if __name__ == "__main__":
    main()
