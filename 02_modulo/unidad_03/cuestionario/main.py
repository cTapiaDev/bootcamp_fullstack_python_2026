import validador
import level
import question as q
import print_preguntas as p
import verify
import time
import os
import sys

limpiar_pantalla = lambda: os.system('cls' if sys.platform == 'win32' else 'clear')

def main():
    print("=== QUIZ: FRONTEND ===")

    opcion = input("Bienvenido al Quiz. ¿Deseas iniciar? (0: Salir, 1: Comenzar): ").strip()
    opcion = validador.validate(['0', '1'], opcion)

    if opcion == '0':
        print('Nos vemos pronto!')
        time.sleep(1)
        sys.exit()

    p_level_str = input('¿Cuántas preguntas por nivel deseas responder? (1, 2 o 3): ').strip()
    p_level = int(validador.validate(['1', '2', '3'], p_level_str))

    n_pregunta = 1
    preguntas_totales = p_level * 3
    continuar = 'y'

    while continuar == 'y' and n_pregunta <= preguntas_totales:
        limpiar_pantalla()
        print(f"Pregunta {n_pregunta} de {preguntas_totales}")

        dificultad = level.choose_level(n_pregunta, p_level)
        print(f"Nivel: {dificultad.capitalize()}\n")

        enunciado, alternativas = q.choose_q(dificultad)
        p.print_pregunta(enunciado, alternativas)

        respuesta = input("\nEscoge tu alternativa (A, B, C o D): ").strip().lower()
        respuesta = validador.validate(['a', 'b', 'c', 'd'], respuesta)

        es_correcta = verify.verificar(alternativas, respuesta)

        if not es_correcta:
            print("\nReprobado!!")
            break

        print("\n¡Excelente! Avanza a la siguiente ronda")
        time.sleep(1.5)

        if n_pregunta < preguntas_totales:
            continuar = input("\n¿Deseas continuar? (y/n): ").strip().lower()
            continuar = validador.validate(['y', 'n'], continuar)
            if continuar == 'n':
                print("Nos vemos pronto!")
                break

        n_pregunta += 1

    if n_pregunta > preguntas_totales:
        limpiar_pantalla()
        print('¡Felicidades! Has respondido todas las preguntas correctamente.')

if __name__ == '__main__':
    main()