import json

class Producto:
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio

    __str__ = lambda self: f"Producto instanciado -> {self.nombre} | Costo: ${self.precio}"


preparar_entorno = lambda ruta: open(ruta, "w").write(
    '{"nombre": "Mouse Gamer", "precio": 25000}\n'
    '{"nombre": "Teclado", "precio": 45000}\n'
    '{"nombre": "Monitor", "precio": 150000}\n'
)

def main() -> None:
    archivo_fuente = "productos.txt"
    preparar_entorno(archivo_fuente)

    instancias: list[Producto] = []

    # Convertir archivo a objetos
    with open(archivo_fuente, "r") as productos:
        linea = productos.readline()

        while linea:
            data_producto = json.loads(linea)

            nuevo_producto = Producto(data_producto.get("nombre"), data_producto.get("precio"))
            instancias.append(nuevo_producto)

            linea = productos.readline()

    print(f"Total de objetos en memoria: {len(instancias)}\n")
    for obj in instancias:
        print(obj)

if __name__ == "__main__":
    main()