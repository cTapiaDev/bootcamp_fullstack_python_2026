import random

MOVIMIENTOS = {
    '1': {'nombre': 'Jab rápido', 'dano': 10, 'defensa': False},
    '2': {'nombre': 'Gancho', 'dano': 25, 'defensa': False},
    '3': {'nombre': 'Guardia cerrada', 'dano': 0, 'defensa': True}
}

OPCIONES_CPU = [
    {'nombre': 'Jab rápido', 'dano': 10, 'defensa': False},
    {'nombre': 'Gancho', 'dano': 20, 'defensa': False},
    {'nombre': 'Guardia cerrada', 'dano': 0, 'defensa': True}
]

def generar_barra(salud):
    bloques_llenos = salud // 10
    bloques_vacios = (100 - salud) // 10

    bloques_llenos = max(0, bloques_llenos)
    bloques_vacios = min(10, bloques_vacios)

    return ('█' * bloques_llenos) + ('░' * bloques_vacios)



def main():
    print('\n=========================================')
    print('           SIMULADOR DE BOXEO              ')
    print('==========================================')

    salud_jugador = 100
    salud_cpu = 100
    round_actual = 1

    
    while salud_jugador > 0 and salud_cpu > 0:
        print(f'\n--- ROUND {round_actual} ---')
        print('1: Jab rápido (Daño: 10)')
        print('2: Gancho (Daño: 25)')
        print('3: Guardia cerrada (Bloqueo)')

        opcion_jugador = input('Ingresa tu opción (1, 2 o 3):\n> ')

        while opcion_jugador not in MOVIMIENTOS:
            print('Opción inválida. Te quedaste congelado por miedo.')
            opcion_jugador = input('Ingresa tu opción (1, 2 o 3):\n> ')

        mov_jugador = MOVIMIENTOS[opcion_jugador].copy()

        if opcion_jugador == '2' and not random.choice([True, False]):
            mov_jugador['nombre'] = 'Gancho (¡¡FALLÓ!!)'
            mov_jugador['dano'] = 0

        mov_cpu = random.choice(OPCIONES_CPU)

        print('\n=========================================')
        print('          INTERCAMBIO DE GOLPES            ')
        print('==========================================')
        print(f'Utilizaste: {mov_jugador['nombre']}')
        print(f'Rival utilizó: {mov_cpu['nombre']}')

        if mov_cpu['defensa'] and mov_jugador['dano'] > 0:
            print('\n¡El rival bloqueó tu ataque de forma perfecta!')
            mov_jugador['dano'] = 0

        if mov_jugador['defensa'] and mov_cpu['dano'] > 0:
            print('\n¡Levantaste la guardia y bloqueaste el ataque!')
            mov_cpu['dano'] = 0

        salud_jugador -= mov_cpu['dano']
        salud_cpu -= mov_jugador['dano']

        salud_jugador = max(0, salud_jugador)
        salud_cpu = max(0, salud_cpu)

        print('\n=========================================')
        print('           RESULTADO DEL ROUND             ')
        print('==========================================')
        print(f'Tú     [{generar_barra(salud_jugador)}] {salud_jugador}/100 HP\n')
        print(f'Rival  [{generar_barra(salud_cpu)}] {salud_cpu}/100 HP')
        print('==========================================')

        round_actual += 1

    if salud_jugador > salud_cpu:
        print("¡KO! ¡Ganaste la Pelea!")
    elif salud_cpu > salud_jugador:
        print('¡KO! El rival te conectó más duro. Entrena tu guardia.')
    else:
        print('¡Doble KO! Empate técnico.')


if __name__ == '__main__':
    main()