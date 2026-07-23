def generar_mapa(filas, columnas):
    return [['L' for _ in range(columnas)] for _ in range(filas)]

def mostrar_mapa(mapa):
    print("\n--- MAPA DE ASIENTOS ---")
    print("  " + " ".join([str(i+1) for i in range(len(mapa[0]))]))

    for i, fila in enumerate(mapa):
        letra_fila = chr(65 + i)
        print(f"{letra_fila} " + " ".join(fila))
    print("----------------")

def reserva_asientos(mapa, fila_str, columna_int):
    fila_idx = ord(fila_str.upper()) - 65
    col_idx = columna_int - 1

    if fila_idx < 0 or fila_idx >= len(mapa) or col_idx < 0 or col_idx >= len(mapa[0]):
        print("Error: Asiento inexistente.")
        return False

    if mapa[fila_idx][col_idx] == 'L':
        mapa[fila_idx][col_idx] = 'X'
        print(f'Éxito: Asiento {fila_str.upper()}{columna_int} reservado correctamente.')
        return True
    else:
        print("Error: El asiento ya se encuentra ocupado")
        return False

def estadisticas_asientos(mapa):
    libres = sum([1 for fila in mapa for asiento in fila if asiento == 'L'])
    ocupados = sum([1 for fila in mapa for asiento in fila if asiento == 'X'])
    return libres, ocupados

def main():
    mapa_cine = generar_mapa(8, 8)
    precio_entrada = 4500
    total_recaudado = 0
    ejecutando = True

    while ejecutando:
        mostrar_mapa(mapa_cine)
        libres, ocupados = estadisticas_asientos(mapa_cine)
        print(f"Asientos Libres: {libres} | Ocupados: {ocupados} | Recaudación: {total_recaudado}")

        print('\n1. Reservar un asiento')
        print('2. Salir del sistema')
        opcion = input('> ')

        if opcion == '1':
            entrada_fila = input('Ingrese la letra de la fila (A-H): ').strip()
            entrada_col = input('Ingrese el número de columna (1-8): ').strip()

            if entrada_col.isnumeric():
                if reserva_asientos(mapa_cine, entrada_fila, int(entrada_col)):
                    total_recaudado += precio_entrada
            else:
                print("Error: La columna debe ser un número entero (1-8).")

        elif opcion == '2':
            print('Cerrando sistema de reservas...')
            ejecutando = False
        else:
            print('Opción inválida')


if __name__ == '__main__':
    main()