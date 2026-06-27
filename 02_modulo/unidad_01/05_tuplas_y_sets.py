# Tuplas: Estructuras Inmutables
configuracion_servidor = ("192.168.1.1", 8080, 'admin')
print(f"Tupla de configuración: {configuracion_servidor}")
print(f"Tipo de dato: {type(configuracion_servidor)}\n")

# Desempaquetamiento (Unpacking)
# Puedo asignar los valores de la tupla en variables individuales.
direccion_ip, puerto, usuario = configuracion_servidor
print(f"- IP: {direccion_ip}")
print(f"- Puerto: {puerto}")
print(f"- Usuario: {usuario}\n")

# Inmutabilidad
try:
    configuracion_servidor[1] = 9090
except TypeError as error:
    print(f"Error esperado: {error}. Las tuplas no soportan asignación de ítems.\n")


# Sets: Conjuntos sin Duplicados
correos_base_datos = {
    "usuario1@gmail.com",
    "usuario2@gmail.com",
    "usuario3@gmail.com",
    "admin@gmail.com",
    "usuario2@gmail.com"
}

print(f"Set de datos: {correos_base_datos}")
print(f"Cantidad de correos: {len(correos_base_datos)}\n")

# Transformación de Lista a Set
encuesta_colores = ["rojo", "azul", "rojo", "verde", "azul", "amarillo", "rojo"]
print(f"Lista original con {len(encuesta_colores)} respuestas: {encuesta_colores}")

colores_unicos = set(encuesta_colores)
print(f"Colores únicos: {colores_unicos}")