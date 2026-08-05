from entidades import LibroFisico

class ItemVenta:
    def __init__(self, producto: LibroFisico, cantidad: int) -> None:
        self.__producto = producto
        self.__cantidad = cantidad

    @property
    def producto(self) -> LibroFisico:
        return self.__producto

    @property
    def cantidad(self) -> int:
        return self.__cantidad

    @property
    def subtotal(self) -> int:
        return self.__producto.precio * self.__cantidad

    def __str__(self) -> str:
        return f"- {self.producto.titulo} (x{self.cantidad}) -> Subtotal: ${self.subtotal}"


class DetalleVenta:
    def __init__(self) -> None:
        self.__items: list[ItemVenta] = []

    def agregar_item(self, item: ItemVenta) -> None:
        self.__items.append(item)

    @property
    def items(self) -> list[ItemVenta]:
        return self.__items

    def calcular_total(self) -> int:
        return sum(item.subtotal for item in self.__items)

    def __str__(self) -> str:
        if not self.__items:
            return "No hay artículos en el detalle."
        return "\n".join(str(item) for item in self.__items)


class Venta:
    def __init__(self, cliente: str) -> None:
        self.cliente = cliente
        self.__detalle = DetalleVenta() # Proceso de Composición

    @property
    def detalle(self) -> DetalleVenta:
        return self.__detalle

    # Proceso de Colaboración
    def registrar_producto(self, producto: LibroFisico, cantidad: int) -> None:
        nuevo_item = ItemVenta(producto, cantidad)
        self.__detalle.agregar_item(nuevo_item)

    def imprimir_recibo(self) -> None:
        print(f"\n{'='*30}")
        print(f"RECIBO DE VENTA - CLIENTE: {self.cliente}")
        print(f"{'='*30}")
        print(self.__detalle)
        print(f"{'='*30}")
        print(f"TOTAL A PAGAR: ${self.__detalle.calcular_total()}")
        print(f"{'='*30}\n")