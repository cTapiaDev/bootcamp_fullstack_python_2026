print("="*50)
print("Construcción de Diccionarios con ZIP")
print("="*50)

claves = ['nombre', 'apellido', 'edad', 'altura']
valores = ['Juan', 'Pérez', 33, 1.75]

usuario = {k: v for k, v in zip(claves, valores)}
print(f"Diccionario generado desde dos listas:\n {usuario}")

print("\n" + "="*50)
print("Ejercicio: Países y filtrado")
print("="*50)

paises = ["México", "Chile", "España"]
usuarios = [70, 50, 55]

diccionario_paises = {k: v for k, v in zip(paises, usuarios)}
print(f"Diccionario de países: {diccionario_paises}")

paises_filtrados = {k: v for k, v in diccionario_paises.items() if v < 60}
print(f"Países con menos de 60 usuarios: {paises_filtrados}")


print("\n" + "="*50)
print("Ejercicio: Ventas")
print("="*50)

ventas = {
    'Octubre': 65000,
    'Noviembre': 68000,
    'Diciembre': 72000
}
print(f"Ventas base: {ventas}")

ventas_incrementadas = {mes: monto * 1.10 for mes, monto in ventas.items()}
print(f"Ventas proyectadas (+10%): {ventas_incrementadas}")

ventas_disminuidas = {mes: monto * 0.80 for mes, monto in ventas.items()}
print(f"Ventas en recesión (-20%): {ventas_disminuidas}")