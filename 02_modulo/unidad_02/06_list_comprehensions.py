# Sintaxis base: [fórmula for variable in iterable]

print("="*50)
print("Generación de Números Pares")
print("="*50)

n = 10
# --- Método tradicional ---
lista_par_tradicional = []

for i in range(n):
    lista_par_tradicional.append(2 * i + 2)

print(f"Tradicional:\t {lista_par_tradicional}")

# --- Método Comprehension ---
lista_par_compre = [2 * i + 2 for i in range(n)]

print(f"Comprehension:\t {lista_par_compre}")

print("\n" + "="*50)
print("Transformación de Tipos de Datos (Casting)")
print("="*50)

datos_texto = ["15", "20", "35", "100", "50"]
print(f"Datos originales (str): {datos_texto}")

# --- Método Tradicional ---
datos_numeros_trad = []
for dato in datos_texto:
    datos_numeros_trad.append(int(dato))

print(f"Tradicional:\t {datos_numeros_trad}")

# --- Método Comprehension ---
datos_numeros_comp = [int(dato) for dato in datos_texto]
print(f"Comprehension:\t {datos_numeros_comp}")

print("\n" + "="*50)
print("Operaciones Matemáticas")
print("="*50)

temperaturas_celsius = [0, 10, 20, 30, 40]
print(f"Temperaturas en C°: {temperaturas_celsius}")

temperaturas_fahrenheit = [(temp * 9/5) + 32 for temp in temperaturas_celsius] 
print(f"Temperaturas en °F: {temperaturas_fahrenheit}")

print("\n" + "="*50)
print("Manipulación de Strings")
print("="*50)

nombres_sucios = ["    juan", "ANA    ", " pEdRo ", "luisa"]
print(f"Nombres sin formato: {nombres_sucios}")

nombres_limpios = [nombre.strip().capitalize() for nombre in nombres_sucios]
print(f"Nombres formateados: {nombres_limpios}")