import os

crear_archivo_prueba = lambda ruta: open(ruta, "w").write("Linea 1: Inicio\nLinea 2: Medio\nLinea 3: Fin\n")

def main() -> None:
    ruta_archivo = "demo_lectura.txt"
    crear_archivo_prueba(ruta_archivo)

    # Método 1: Apertura tradicional (con read())
    archivo_manual = open(ruta_archivo)
    contenido_completo = archivo_manual.read()
    print(repr(contenido_completo))
    archivo_manual.close()

    print("\n")

    # Método 2: Context Manager y readlines()
    with open(ruta_archivo, "r") as archivo_lineas:
        lineas = archivo_lineas.readlines()
        print(lineas)

    # Método 3: Iteración directa
    with open(ruta_archivo, "r") as archivo_iterado:
        for linea in archivo_iterado:
            print(linea.strip())

        
if __name__ == "__main__":
    main()