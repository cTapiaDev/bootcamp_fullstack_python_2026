# Ciclo FOR
# Funcionalidad RANGE() -> es un generador de secuencias numéricas

print('a) range(stop) -> 1 parámetro:')
for numero in range(5):
    print(f'Generando token de sesión: {numero}')

print('\nb) range(start, stop) -> 2 parámetros:')
for dia in range(1, 6):
    print(f'Procesando métricas del día {dia} de la semana.')

# Siempre el stop es el número dado menos uno

print('\nc) range(start, stop, step) -> 3 parámetros (Salto):')
# step es el parámetro que define como avanza la iteración
for puerto in range(3000, 3011, 2):
    print(f'Escaneando puerto seguro: {puerto}')

print('\nd) range() en reversa:')
for cuenta_regresiva in range(3, 0, -1):
    print(f'Volcado de memoria en {cuenta_regresiva}...')

# Iterando sobre Listas (For Each)
stack_tecnologico = ['Vue 3', 'Svelte', 'Astro', 'React']

print('\nLevantando servidores de desarrollo:')
for tech in stack_tecnologico:
    print(f'-> Servidor iniciando en modo vista para {tech.upper()}')

# Iterando sobre Strings
coordenada_vtt = "X:15,Y:42"

print(f'\nAnalizando la cadena de coordenadas: {coordenada_vtt}')
vocales = 0
numeros = 0

for caracter in coordenada_vtt:
    if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
        vocales += 1
    elif caracter.isnumeric():
        numeros += 1

print(f'Análisis completado: Contiene {vocales} vocales y {numeros} números.\n')

# Me permite Modificar valores
precios_netos = [1000, 2500, 5000, 10000]
precios_con_iva = []

IVA = 1.19

for precio in precios_netos:
    calculo = precio * IVA
    precios_con_iva.append(calculo)

print(f'Precios Originales: {precios_netos}')
print(f'Precios Finales: {precios_con_iva}')