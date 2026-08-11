import os

def main() -> None:
    ruta_relativa = "datos_crudos.bin"

    ruta_absoluta = os.path.abspath(ruta_relativa)
    print(f"Trabajando en: {ruta_absoluta}")

    with open(ruta_absoluta, "wb") as archivo_binario:
        archivo_binario.write(b'0101010101' * 21)

    print("\n Lectura por chunks (bloques)")
    chunk_size = 70

    with open(ruta_absoluta, "rb") as archivo:
        chunk = archivo.read(chunk_size)

        iteracion = 1
        while chunk:
            print(f"Chunk {iteracion} leído ({len(chunk)} bytes): {chunk[:10]}...")
            chunk = archivo.read(chunk_size)
            iteracion += 1

    print("\n Renombrar archivo con OS")
    nuevo_nombre = os.path.abspath("datos_procesados.bin")

    if os.path.exists(nuevo_nombre):
        os.remove(nuevo_nombre)

    os.rename(ruta_absoluta, nuevo_nombre)
    print(f"Archivo renombrado a: {nuevo_nombre}")

if __name__ == "__main__":
    main()