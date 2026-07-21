inventario = {
    "espada": 1,
    "escudo": 1,
    "pocion_vida": 5
}
print(f"Inventario: {inventario}")

inventario["mapa"] = 1
print(f"Elemento mapa agregado: {inventario}")

# inventario['pocion_vida'] = 3
inventario['pocion_vida'] -= 2
print(f"Cantidad de 'pocion_vida' cambiada: {inventario}")

item_descartado = inventario.pop('escudo')
print(f"Elemento 'escudo' eliminado (Cantidad perdida: {item_descartado})")

print(f"Inventario Final: {inventario}")