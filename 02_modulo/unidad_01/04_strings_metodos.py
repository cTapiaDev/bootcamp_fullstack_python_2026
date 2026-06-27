
# 1. Strings y sus Métodos
texto_prueba = "    python Es lenguaje versátil ➤ ⚠️  "

print(f"Texto original: {texto_prueba}")
print(f"Mayúsculas: {texto_prueba.upper()}")
print(f"Minúsculas: {texto_prueba.lower()}")
print(f"Capitalize: {texto_prueba.title()}")
print(f"Strip (Trim): {texto_prueba.strip()}")
print(f"Trim Left: {texto_prueba.lstrip()}")
print(f"Trim Right: {texto_prueba.rstrip()}\n")

# .count()
ocurrencias_e = texto_prueba.lower().count("e")
print(f"La letra 'e' aparece {ocurrencias_e} veces en el texto\n")

longitud_text = len(texto_prueba)
print(f"La longitud total del string es: {longitud_text} caracteres.")

# Integración de listas
lenguajes_programacion = ['Python', 'JavaScript', 'C++', 'Ruby', 'Java']
separador = ' | '
lista_unida = separador.join(lenguajes_programacion)
print(f"Lista unida con separador: {lista_unida}")