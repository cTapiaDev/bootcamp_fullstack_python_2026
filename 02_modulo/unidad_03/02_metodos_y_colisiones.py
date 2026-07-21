diccionario_a = {
    "nombre": "Alejandra",
    "apellido": "López",
    "edad": 33,
    "altura": 1.55
}

diccionario_b = {
    "mascota": "miti",
    "ejercicio": "bicicleta",
    "altura": 155
}

diccionario_a.update(diccionario_b)

print(f"Diccionario unificado: {diccionario_a}")

# Métodos keys(), values() e items()
computador = {
    'notebook': 490000,
    'tablet': 120000,
    'cargador': 10000,
    'iphone': 500000,
}

print(f"\nClaves: {computador.keys()}")
print(f"Valores: {computador.values()}")
print(f"Items: {computador.items()}")

busqueda = computador.get('iphone', 'No se encuentra el elemento solicitado')
print(f"Buscando iphone: {busqueda}")
# El método get() me permite acceder al valor de un elemento del diccionario

# Métodos list() - items()
lista_desde_dict = list(computador.items())
print(f"De Diccionario a Tupla: {lista_desde_dict}")

dict_desde_lista = dict([('k1', 5), ('k2', 7)])
print(f"De Tupla a Diccionario: {dict_desde_lista}")