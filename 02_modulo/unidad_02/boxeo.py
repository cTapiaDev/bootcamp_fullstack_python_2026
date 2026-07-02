import random

print('\n=========================================')
print('           SIMULADOR DE BOXEO              ')
print('==========================================')

salud_jugador = 100
salud_cpu = 100

print('\n--- TU TURNO: Elige tu movimiento ---')
print('1: Jab rápido (Daño: 10)')
print('2: Gancho (Daño: 25)')
print('3: Guardia cerrada (Bloqueo)')

opcion_jugador = input('Ingresa tu opción (1, 2 o 3):\n> ')

movimiento_jugador = ''
dano_jugador = 0
esta_defendiendo_jugador = False

if opcion_jugador == '1':
    movimiento_jugador = 'Jab Rápido'
    dano_jugador = 10

elif opcion_jugador == '2':
    acierta_gancho = random.choice([True, False])

    if acierta_gancho:
        movimiento_jugador = 'Gancho'
        dano_jugador = 25
    else:
        movimiento_jugador = 'Gancho (¡¡FALLÓ!!)'
        dano_jugador = 0

elif opcion_jugador == '3':
    movimiento_jugador = 'Guardia cerrada'
    esta_defendiendo_jugador = True

else: 
    print('\nOpción inválida. Te quedaste congelado por miedo.')
    movimiento_jugador = 'Congelado'

# Opciones de la Máquina
opcion_maquina = ['Jab rápido', 'Gancho', 'Guardia']
movimiento_cpu = random.choice(opcion_maquina)

dano_cpu = 0
esta_defendiendo_cpu = False

if movimiento_cpu == 'Jab rápido':
    dano_cpu = 10
elif movimiento_cpu == 'Gancho':
    dano_cpu = 20
elif movimiento_cpu == 'Guardia':
    esta_defendiendo_cpu = True

print('\n=========================================')
print('          INTERCAMBIO DE GOLPES            ')
print('==========================================')
print(f'Utilizaste: {movimiento_jugador}')
print(f'Rival utilizó: {movimiento_cpu}')

if esta_defendiendo_cpu:
    print('\n¡El rival bloqueó tu ataque de forma perfecta!')
    dano_jugador = 0

if esta_defendiendo_jugador:
    print('\n¡Levantaste la guardia y bloqueaste el ataque!')
    dano_cpu = 0

salud_jugador = salud_jugador - dano_cpu
salud_cpu = salud_cpu - dano_jugador

if salud_jugador < 0:
    salud_jugador = 0
if salud_cpu < 0:
    salud_cpu = 0

bloques_llenos_jugador = salud_jugador // 10
bloques_vacios_jugador = (100 - salud_jugador) // 10

bloques_llenos_cpu = salud_cpu // 10
bloques_vacios_cpu = (100 - salud_cpu) // 10

barra_jugador = ('█' * bloques_llenos_jugador) + ('░' * bloques_vacios_jugador)
barra_cpu = ('█' * bloques_llenos_cpu) + ('░' * bloques_vacios_cpu)

print('\n=========================================')
print('           RESULTADO DEL ROUND             ')
print('==========================================')
print(f'Tú     [{barra_jugador}] {salud_jugador}/100 HP\n')
print(f'Rival  [{barra_cpu}] {salud_cpu}/100 HP')
print('==========================================')

if salud_jugador > salud_cpu:
    print("¡Ganaste este round!")
elif salud_cpu > salud_jugador:
    print('El rival te conectó más duro. Cuidado con esa guardia.')
else:
    print('Empate. Ninguno cedió terreno.')