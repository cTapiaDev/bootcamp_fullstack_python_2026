import math

operador_x = 17
operador_y = 5

suma = operador_x + operador_y
resta = operador_x - operador_y
multiplicacion = operador_x * operador_y

division_flotante = operador_x / operador_y
division_entera = operador_x // operador_y # Esta forma de dividir aproxima de manera automática
resto_modulo = operador_x % operador_y
exponenciacion = operador_y ** 3


print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División Estándar (/): {division_flotante}")
print(f"División Entera (//): {division_entera}")
print(f"Módulo o Resto (%): {resto_modulo}")
print(f"Potencia (**): {exponenciacion}\n")

# 2. Procedencia de Operadores
# Paréntesis -> Exponentes -> Multiplicación/División -> Adición/Sustracción
calculo_complejo_1 = 5 + 3 * 2 ** 2
calculo_complejo_2 = (5 + 3) * 2 ** 2

print(f"Precedencia sin agrupar: {calculo_complejo_1}")
print(f"Precedencia agrupada: {calculo_complejo_2}")

# 3. Casteo de Datos
print("\n--- Conversión de Tipos ---")

numero_string = "15.75"
print(f"numero_string: {type(numero_string)}")

numero_casteado = float(numero_string)
print(f"numero_casteado: {type(numero_casteado)}")

# 4. Librería math
valor_decimal = 4.23

techo = math.ceil(valor_decimal)     # Aproxima al entero superior
piso = math.floor(valor_decimal)     # Aproxima al entero inferior
raiz = math.sqrt(16)

print(f"\nMétodos de math aplicados a {valor_decimal}")
print(f"math.ceil() : {techo}")
print(f"math.floor() : {piso}")
print(f"math.sqrt() : {raiz}")