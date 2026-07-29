import sys
from clima import Clima
from dron import Dron
from enjambre import Enjambre

def main():
    print("=== SIMULADOR DE DRONES ===")

    mi_flota = Enjambre("PyTech Alpha")

    dron_1 = Dron("DRN-001")
    dron_2 = Dron("DRN-002")

    mi_flota.registrar_dron(dron_1)
    mi_flota.registrar_dron(dron_2)

    while True:
        viento_actual = Clima.generar_viento_actual()
        print(f"\nCondiciones actuales: Viento a {viento_actual} km/h")

        print("\nOpciones:")
        print("1. Enviar dron")
        print("2. Despliegue del enjambre")
        print("3. Reparar/Recargar dron")
        print("4. Ver reporte de flota")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            if not Clima.es_seguro_volar(viento_actual):
                continue

            id_dron = input("Ingrese el ID del dron (ej. DRN-001): ").strip().upper()
            dron_seleccionado = next((d for d in mi_flota.drones if d.identificador == id_dron), None)

            if dron_seleccionado:
                try:
                    distancia = int(input("Distancia de la misión (km): "))
                    peso = int(input("Peso de la carga (kg): "))
                    dron_seleccionado.volar(distancia, peso)
                except ValueError:
                    print("Ingrese valores numéricos válidos.")
            else:
                print("Dron no encontrado.")

        elif opcion == '2':
            if not Clima.es_seguro_volar(viento_actual):
                continue

            try:
                distancia = int(input("Distancia de la misión conjunta (km): "))
                peso = int(input("Peso de la carga por dron (kg): "))
                mi_flota.despliegue_masivo(distancia, peso)
            except ValueError:
                print("Ingrese valores numéricos válidos.")

        elif opcion == '3':
            id_dron = input("Ingrese el ID del dron a reparar (ej. DRN-001): ").strip().upper()
            dron_seleccionado = next((d for d in mi_flota.drones if d.identificador == id_dron), None)

            if dron_seleccionado:
                dron_seleccionado.reparar()
            else:
                print("Dron no encontrado.")

        elif opcion == '4':
            mi_flota.reporte_general()

        elif opcion == '0':
            print("Apagando sistemas de la flota...")
            sys.exit()

        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()