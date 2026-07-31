import sys
from modelos import ExamenAlternativas, ProyectoPractico
from gestor import GestorEvaluaciones

PAUTA = {1: "A", 2: "C", 3: "B", 4: "D", 5: "A"}

def ingresar_examen_teorico() -> ExamenAlternativas:
    print("\n[Ingreso de Examen Teórico]")
    id_ent = input("ID de entrega (Ej. EX-01): ")
    nombre = input("Nombre del Alumno: ")

    print("Ingrese las alternativas del alumno (A-D): ")
    respuestas_alumno = {}
    for i in range(1, 6):
        resp = input(f"Pregunta {i}: ").strip().upper()
        respuestas_alumno[i] = resp

    return ExamenAlternativas(id_ent, nombre, "Frontend Vue 3", PAUTA, respuestas_alumno)

def ingresar_proyecto_practico() -> ProyectoPractico:
    print("\n[Ingreso de Proyecto Práctico]")
    id_ent = input("ID de entrega (Ej. PR-01): ")
    nombre = input("Nombre del Alumno: ")
    url = input("URL del repositorio (Ej. github.com/user/repo): ")

    try:
        ui = float(input("Puntaje Rúbrica UI (0-100): "))
        arq = float(input("Puntaje Rúbrica Arquitectura (0-100): "))
        logica = float(input("Puntaje Rúbrica Lógica (0-100): "))
    except ValueError:
        print("Valores inválidos. Se asignará 0 por defecto")
        ui, arq, logica = 0.0, 0.0, 0.0

    rubrica = {"UI": ui, "Arquitectura": arq, "Logica": logica}

    return ProyectoPractico(id_ent, nombre, "Mobile Android", url, rubrica)

def main():
    sistema = GestorEvaluaciones()

    while True:
        print("\n=== PLATAFORMA DE EVALUACIÓN ===")
        print("1. Cargar nuevo Examen Teórico")
        print("2. Cargar nuevo Proyecto Práctico")
        print("3. Ejecutar Corrección Masiva")
        print("4. Ejecutar Auditoría")
        print("5. Ver Boletín General")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            examen = ingresar_examen_teorico()
            sistema.registrar_nueva_entrega(examen)

        elif opcion == '2':
            proyecto = ingresar_proyecto_practico()
            sistema.registrar_nueva_entrega(proyecto)

        elif opcion == '3':
            sistema.corregir_todas_las_entregas()

        elif opcion == '4':
            sistema.auditar_proyectos()

        elif opcion == '5':
            sistema.listar_boletin_general()

        elif opcion == '0':
            print('Cerrando Sistema...')
            sys.exit()

        else:
            print('Opción no válida. Intente nuevamente.')

if __name__ == '__main__':
    main()