texto = "Hola Mundo"
print(texto)
print(f"El largo del texto es: {len(texto)}")

# Sintaxis básica de función
def nombre_funcion():
    print("Hola desde la función")
    pass # Sirve para indicar que la función termina, pero no es necesario

nombre_funcion()

# Principio DRY (Don't Repeat Yourself)
def imprimir_menu():
    print("Opciones: ")
    print("1). De acuerdo")
    print("2). En desacuerdo")
    print("3). No me interesa")

# print("Mostrar el menú una vez:")
# imprimir_menu()

# print("\nMostrar el menú una segunda vez:")
# imprimir_menu()

preguntas_producto = ['¿El diseño es atractivo?', '¿El precio es adecuado?', '¿Lo recomendaría?']
respuestas_producto = []

print("--- INICIANDO ENCUESTA DE PRODUCTO ---")

for p in preguntas_producto:
    print(p)
    imprimir_menu()
    respuestas_producto.append(input('>'))

for i in range(len(preguntas_producto)):
    print(f"La respuesta a la pregunta {i+1} fue {respuestas_producto[i]}")


