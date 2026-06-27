# Diccionarios - Estructuras (Clave-Valor)
# "clave": valor
perfil_estudiante = {
    "nombre": "Andrés",
    "apellido": "Gómez",
    "edad": 28,
    "carrera": "Data Science",
    "promedio": 6.8
}

print(f"Diccionario: {perfil_estudiante}")

print(f"Nombre del estudiante: {perfil_estudiante['nombre']}")
print(f"Carrera actual: {perfil_estudiante['carrera']}\n")

# Si tengo claves repetidas, la segunda sobreescribe a la primera
diccionario_colisiones = {
    "id_producto": 101,
    "nombre": "Teclado",
    "precio": 25000,
    "precio": 990
}

print(f"Diccionario: {diccionario_colisiones}")
print(f"Precio final es: {diccionario_colisiones['precio']}\n")

# KeyError
try:
    valor_error = perfil_estudiante['Nombre']
except KeyError as err:
    print(f"Error de acceso (KeyError): La clave {err} no se encuentra en el diccionario")

# Nos permite inyectar datos sin problema
perfil_estudiante["ciudad"] = "Santiago"
perfil_estudiante["promedio"] = 6.5

print(f"Perfil Actualizado: {perfil_estudiante}")