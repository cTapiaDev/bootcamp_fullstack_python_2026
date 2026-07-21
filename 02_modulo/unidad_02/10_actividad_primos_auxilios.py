# Actividad 2 - Árbol de decisiones de Primeros Auxilios
# Explicación:
# Construiremos una aplicación que entregue los distintos
# pasos a seguir dependiendo de las respuestas del usuario en tiempo real

estimulos = input("¿La persona responde? (si/no): ").strip().lower()

if estimulos == 'si':
    print("Llevarlo al hospital más cercano.")
else:
    respira = input("¿Respira? (si/no): ").strip().lower()

    if respira == 'si':
        print("Acomodarlo en una posición para mejor ventilación.")
    else:
        print("Administrar 5 ventilaciones y llamar Ambulancia.")

        emergencia_activa = True
        while emergencia_activa:
            signos = input("¿Signos de vida? (si/no): ").strip().lower()

            if signos == 'no':
                print("Administrar compresiones hasta que llegue la ambulancia.")
            else:
                print("Esperar ambulancia")

            ambulancia = input("¿Llegó la ambulancia? (si/no): ").strip().lower()

            if ambulancia == 'si': emergencia_activa = False

print("\nFin de la Asistencia")