import random

def jugar_adivinanza():
    print("¡Bienvenido al juego de adivinar el número!")
    print("El programa pensará un número entre 1 y un máximo dependiendo de la dificultad")
    print("Intenta adivinarlo con la menor cantidad de intentos posible.\n")

    while True:
        nivel = input("Elige un nivel (fácil, medio, difícil): ").lower()
        if (nivel == "fácil"):
            max_num = 50
            break
        elif nivel == "medio":
            max_num = 100
            break
        elif nivel == "difícil":
            max_num = 500
            break
        else:
            print("Nivel no válido. Intenta de nuevo.")

    numero_secreto = random.randint(1, max_num)
    intentos = 0

    while True:
        try:
            adivinanza = int(input(f"Adivina un número entre 1 y {max_num}: "))
            intentos += 1
            if adivinanza < numero_secreto:
                print("Demasiado bajo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto.")
            else:
                print(f"¡Felicidades! Adivinaste en {intentos} intentos.\n")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

def main():
    while True:
        jugar_adivinanza()
        jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra_vez != 's':
            print("¡Gracias por jugar! ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
