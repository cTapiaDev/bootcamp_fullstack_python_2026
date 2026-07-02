import math
import random

nombre_cliente = input('Ingrese su nombre:\n> ')
distancia_km = float(input('Ingrese la distancia en kilómetros (Ej. 2.5):\n> '))

print('\n¿El cliente posee suscripción "Plus" activa?')
print('1: Sí')
print('2: No')
opcion_plus = input('> ')

es_usuario_plus = opcion_plus == '1'

print('\n--- MENÚ DISPONIBLE ---')
print('1: Tempura Rolls (30 piezas) - $15.000')
print('2: Pizza Familiar Bordequeso - $18.500')
print('3: Combo Hamburguesas y Nuggets - $12.000')

opcion_menu = input('\nSeleccione un plato (1, 2 o 3):\n> ')

precio_plato = 0
nombre_plato = ''

if opcion_menu == '1':
    precio_plato = 15000
    nombre_plato = 'Tempura Rolls'
elif opcion_menu == '2':
    precio_plato = 18500
    nombre_plato = 'Pizza Familiar Bordequeso'
elif opcion_menu == '3':
    precio_plato = 12000
    nombre_plato = 'Combo Fast Food'
else:
    print('\nError: Selección no válida.')
    precio_plato = 12000
    nombre_plato = 'Combo Fast Food'

lista_regalos = ['Bebida 1.5L', 'Porción de Papas Fritas', 'Postre de Chocolate', 'Nuggets', '-']
regalo_sorpresa = random.choice(lista_regalos)

costo_envio = 1000 + (500 * distancia_km)
aplica_envio_gratis = es_usuario_plus or (precio_plato >= 16000)

if aplica_envio_gratis:
    costo_envio = 0

total_pagar = precio_plato + costo_envio

tiempo_estimado_raw = 15 + (4 * distancia_km)
tiempo_final = math.ceil(tiempo_estimado_raw)

repartidores_disponibles = ['Juan', 'María', 'Felipe', 'Andrés']
repartidor_asignado = random.choice(repartidores_disponibles)

print('\n=====================================')
print('           BOLETA DE PAGO              ')
print('======================================')
print(f'Cliente     : {nombre_cliente}')
print(f'Pedido      : {nombre_plato} (${precio_plato})')

if aplica_envio_gratis:
    print('Costo de Envío: $0 (Promoción aplicada)')
else:
    print(f'Costo de Envío: ${costo_envio:.0f}')

if regalo_sorpresa != '-':
    print(f'🎁 Regalo Extra : {regalo_sorpresa}')

print(f'TOTAL A PAGAR : ${total_pagar:.0f}')
print('---------------------------------------')
print(f'Repartidor    : {repartidor_asignado}')
print(f'Tiempo de entrega estimado: {tiempo_final} minutos.')
print('=====================================')