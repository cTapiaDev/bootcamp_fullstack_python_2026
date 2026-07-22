import sys

nombre = sys.argv[1]
apellido = sys.argv[2]

resultado_1 = f"Mi nombre es {nombre}"
resultado_2 = f"Mi apellido es {apellido}"
resultado_3 = f"El nombre de este archivo es {sys.argv[0]}"

print(resultado_1)
print(resultado_2)
print(resultado_3)

opcion_guardar = input("\n¿Desea guardar estos resultados en un archivo local? (si/no)").strip().lower()

if opcion_guardar == 'si':
    with open("salida.txt", "w", encoding="utf-8") as archivo:
        archivo.write(resultado_1 + "\n")
        archivo.write(resultado_2 + "\n")
        archivo.write(resultado_3 + "\n")

print("Archivo generado exitosamente!")