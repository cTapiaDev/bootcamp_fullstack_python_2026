import sys
from evento import Evento

dibujar_seperador = lambda: print("-" * 45)
formatear_moneda = lambda valor: f"${valor:,}".replace(',', '.')

def main():
    print("=== TICKETS - PRECIOS DINÁMICOS ===")

    tech = Evento(nombre="Festival PyTech 2026", capacidad_maxima=5, precio_inicial=10000)
    print(f"Evento '{tech.nombre}' creado. Capacidad: {tech.capacidad_maxima} personas.")

    while True:
        dibujar_seperador()
        print(f"Precio Actual del Ticket: {formatear_moneda(tech.precio_actual)}")
        print(f"Ocupación: {len(tech.entradas_vendidas)}/{tech.capacidad_maxima}")
        print("\nOpciones:")
        print("1. Comprar Ticket")
        print("2. Ver listado de asistentes")
        print("3. Ver reporte")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            nombre = input("Ingrese su nombre: ").strip().title()
            if nombre:
                tech.procesar_compra(nombre)
            else:
                print("El nombre no puede estar vacío.")

        if opcion == '2':
            if not tech.entradas_vendidas:
                print("Aún no hay entradas vendidas.")
            else:
                print('\n--- LISTA DE ASISTENTES ---')

                for t in tech.entradas_vendidas:
                    estado = "VÁLIDO" if t.es_valido else "ANULADO"
                    print(f"[{t.id_ticket}] {t.nombre_comprador} - Pagó: {formatear_moneda(t.precio_pagado)} ({estado})")

        if opcion == '3':
            neto = tech.calcular_ganancias_netas()
            print('\n--- REPORTE ---')
            print(f"Recaudación Bruta: {formatear_moneda(tech.recaudacion_total)}")
            print(f"Comisión Plataforma ({Evento.comision_plataforma * 100}%): -{formatear_moneda(tech.recaudacion_total - neto)}")
            print(f"Ganancia Neta del Evento: {formatear_moneda(neto)}")

        elif opcion == '0':
            print("Cerrando sistema de ventas...")
            sys.exit()

        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()