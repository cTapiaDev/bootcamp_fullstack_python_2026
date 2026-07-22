# Parámetros: elemento utilizado dentro de la función para realizar cálculos.
# Argumento: valores que tomará el parámetro al ser invocado.

def elevar(base, exponente):
    print(f"El resultado de {base} elevado a {exponente} es: {base**exponente}")

elevar(2, 2)
elevar(3, 3)
elevar(4, 2)

def procesar_saludo(nombre, turno):
    print(f"¡Buenos/as {turno}, {nombre}! Bienvenido/a al sistema.")

procesar_saludo("Ana", "noches")
procesar_saludo("Juan", "tardes")

# Retornos y Retornos Múltiples

def cuadrado_cubo(base):
    cuadrado = base**2
    cubo = base**3
    return cuadrado, cubo

resultado = cuadrado_cubo(2)
print(f"Resultado: {resultado}")

valor_cuadrado, valor_cubo = cuadrado_cubo(2)
print(f"Valor del cuadrado: {valor_cuadrado}")
print(f"Valor del cubo: {valor_cubo}")


def analisis_palabra(palabra):
    largo = len(palabra)
    en_mayusculas = palabra.upper()
    en_minusculas = palabra.lower()
    return largo, en_mayusculas, en_minusculas

# res_largo, res_mayus, res_minus = analisis_palabra("Desarrollo")
# print("\nAnálisis de 'Desarrollo'")
# print(f"Largo: {res_largo} caracteres")
# print(f"Mayúsculas: {res_mayus}")
# print(f"Minúsculas: {res_minus}")

palabras = ['hola', 'adios', 'etc']

for palabra in palabras:
    res_largo, res_mayus, res_minus = analisis_palabra(palabra)
    print(f"\nAnálisis de {palabra}")
    print(f"Largo: {res_largo} caracteres")
    print(f"Mayúsculas: {res_mayus}")
    print(f"Minúsculas: {res_minus}")