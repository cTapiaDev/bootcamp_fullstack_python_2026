lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(lista_de_numeros.__dir__())

colores = ['verde', 'rojo', 'rosa', 'azul']
colores.append('celeste')
print(f"Lista con append: {colores}")

lista_de_numeros.insert(15, 20)
lista_de_numeros.insert(3, 30)
print(f"Lista con insert: {lista_de_numeros}")

color_extraido = colores.pop(3)
print(f"Elemento extraído: {color_extraido}")
print(colores)

animales = ["perros", "gato", "hurón", "erizo"]
numeros = [100, 20, 70, 500]

print(f"Posición de gato: {animales.index('gato')}")
print(f"Posición de 500: {numeros.index(500)}")

# Métodos en Diccionarios
diccionario = {'llave 1': 5}
print(f"Diccionario inicial: {diccionario}")

diccionario['llave 2'] = 9
print(f"Tras agregar llave 2: {diccionario}")

diccionario['llave 2'] = 7
print(f"Tras modificar llave 2: {diccionario}")

# ----------------------

tecnologia = {
    "celular": 140000,
    "notebook": 490000,
    "tablet": 120000,
    "cargador": 10000
}

print(f"\nDiccionario de tecnología: {tecnologia}")

del tecnologia["celular"]
print(f"Tras usar 'del' en celular: {tecnologia}")

valor_eliminado = tecnologia.pop("tablet")
print(f"Valor extraído con pop: {valor_eliminado}")
print(f"Diccionario final: {tecnologia}")