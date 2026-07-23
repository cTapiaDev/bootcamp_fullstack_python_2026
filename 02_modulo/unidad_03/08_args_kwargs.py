# Argumentos Indeterminados
def sumar_numeros(*args):
    suma = 0
    for num in args:
        suma += num
    return suma

print(f"Suma de 3 argumentos: {sumar_numeros(1, 2, 3)}")
print(f"Suma de 5 argumentos: {sumar_numeros(1, 2, 3, 4, 5)}")
print(f"Sin argumentos: {sumar_numeros()}")

# Argumentos Nombrados Indeterminados
def crear_perfil(**kwargs):
    perfil = {}
    for key, value in kwargs.items():
        perfil[key] = value
    return perfil

perfil1 = crear_perfil(nombre='Alice', edad=25, ciudad='Barcelona')
perfil2 = crear_perfil(email="hola@gmail.com", hora="19:54", pais="Chile")

print(perfil1)
print(perfil2)

# ----------------

def get_multiple(diccionario, *claves):
    return {clave: diccionario[clave] for clave in claves if clave in diccionario}

diccionario_prueba = {
    'manzana': 'verde',
    'platano': 'amarillo',
    'frutilla': 'roja'
}

resultado = get_multiple(diccionario_prueba, 'manzana', 'platano', 'pera')
print(resultado)