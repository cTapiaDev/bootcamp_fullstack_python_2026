# Cálculo básico de ganancias
print("--- Calculadora de Ganancias ---")

precio_ticket = float(input("Ingrese el precio del ticket (P):\n> "))
asistentes = int(input("Ingrese el número total de asistentes (A):\n> "))
costos_produccion = float(input("Ingrese los costos de producción (CP):\n> "))

# Ganancias = (P * A ) - CP
ganancias = (precio_ticket * asistentes) + costos_produccion
# int y float pueden interactuar sin problemas, pero el resultado siempre es de tipo float

print(f'\nLas ganancias del evento son: ${ganancias:.2f}')