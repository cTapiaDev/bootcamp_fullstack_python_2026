precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar(diccionario, umbral):
    filtro = {k: v for k, v in diccionario.items() if v > umbral}
    return filtro

resultado_filtro = filtrar(precios, 35000)
print(resultado_filtro)

lista_numeros = [1, 2, 3, 4, 5]
lista_string = ['a', 'b', 'c', 'd', 'e']

def sumar_contar_tipos(lista, funcion):
    tipos = [type(elemento) for elemento in lista]
    opcion = funcion(lista)
    return tipos, opcion

tipo_str, conteo = sumar_contar_tipos(lista_string, len)
tipo_num, suma = sumar_contar_tipos(lista_numeros, sum)

print(f"Tipos: {tipo_str}")
print(f"Resultando de len(): {conteo}")
print(f"\nTipos: {tipo_num}")
print(f"Resultado de sum(): {suma}")