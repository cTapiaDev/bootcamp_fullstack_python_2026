class Producto:
    def __init__(self, nombre: str, precio: int, stock:int = 0) -> None:
        self.__nombre = nombre
        self.__precio = precio
        self.stock = max(0, stock)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def precio(self) -> int:
        return self.__precio

    __eq__ = lambda self, otro: self.nombre.lower() == otro.nombre.lower() if isinstance(otro, Producto) else False
    __add__ = lambda self, cantidad: Producto(self.nombre, self.precio, self.stock + cantidad)
    __sub__ = lambda self, cantidad: Producto(self.nombre, self.precio, self.stock - cantidad)