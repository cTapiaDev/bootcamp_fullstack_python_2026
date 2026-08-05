import random
from personaje import Personaje

def main() -> None:
    print("¡Bienvenido a Gran Fantasía!")
    nombre_jugador = input("Por favor indique nombre de su personaje:\n").strip()

    jugador = Personaje(nombre_jugador)
    print(f"{jugador.estado}")

    print(f"\n¡Oh no!, ¡Ha aparecido un Orco!")
    orco = Personaje("Orco")

    probabilidad = jugador.probabilidad_ganar(orco)
    opcion = Personaje.mostrar_dialogo(probabilidad)

    while opcion == '1':
        resultado_ataque = random.uniform(0, 1)

        if resultado_ataque <= probabilidad:
            print("\n¡Le has ganado al orco, felicidades!")
            print("¡Recibirás 50 puntos de experiencia!")
            jugador.estado = 50
            orco.estado = -30
        else:
            print("\n¡Oh no! ¡El orco te ha ganado!")
            print("¡Has perdido 30 puntos de experiencia!")
            jugador.estado = -30
            orco.estado = 50

        print(f"\n{jugador.estado}")
        print(f"\n{orco.estado}")

        probabilidad = jugador.probabilidad_ganar(orco)
        opcion = Personaje.mostrar_dialogo(probabilidad)

    if opcion == '2':
        print("\n¡Has huido! El orco ha quedado atrás.")
        

if __name__ == "__main__":
    main()