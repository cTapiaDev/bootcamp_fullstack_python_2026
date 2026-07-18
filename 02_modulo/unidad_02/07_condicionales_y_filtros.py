print("="*50)
print("Condicional IF/ELSE")
print("="*50)
# Sintaxis: [expresión1 if condición1 else expresión2 for variable in iterable]

valores = [8, 4, 5, 6, 7, 8, 9]
print(f"Lista de valores: {valores}")

divisibles = ['Divisible' if valor % 2 == 0 else 'No Divisible' for valor in valores]
print(f"Evaluación de paridad: {divisibles}")

notas = [45, 89, 32, 60, 75, 20]
# Si la nota es >= 660 es 'Aprobado', sino 'Reprobado'
estados = ['Aprobado' if nota >= 60 else 'Reprobado' for nota in notas]

print("\n" + "="*50)
print("Condicional IF al Final")
print("="*50)
# Sintais: [expresión for variable in iterable if condición]

lista_mixta = ['Lechuga', 'Tomates', 5, 10, True, False, True, 'Papas', 5.1, 45.2, 1, 2, 0]
print(f"Lista con datos sucios: {lista_mixta}")

solo_textos = [elemento for elemento in lista_mixta if type(elemento) is str]
solo_enteros = [elemento for elemento in lista_mixta if type(elemento) == int]

print(f"Solo Textos (str): {solo_textos}")
print(f"Solo Enteros (int): {solo_enteros}")

print(f"Total de textos recuperados: {len(solo_textos)}")