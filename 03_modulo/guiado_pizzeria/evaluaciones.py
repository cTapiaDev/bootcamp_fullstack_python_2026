from pizza import Pizza

formatear_bool = lambda valor: "Sí" if valor else "No"

# 5.a
print(f"Precio: ${Pizza.precio}")
print(f"Tamaño: {Pizza.tamano}")

# 5.b
resultado_validacion = Pizza.validar_elemento('salsa de tomate', ['salsa de tomate', 'salsa bbq'])
print(f"¿'salsa de tomate' está en la lista?: {resultado_validacion}")

# 5.c
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# 5.d
print(f"\nProteico: {mi_pizza.proteico}")
print(f"Vegetales: {mi_pizza.vegetal_1}, {mi_pizza.vegetal_2}")
print(f"Masa: {mi_pizza.masa}")
print(f"¿Pizza válida?: {formatear_bool(mi_pizza.es_valida)}")

# 5.e
print(Pizza.es_valida)