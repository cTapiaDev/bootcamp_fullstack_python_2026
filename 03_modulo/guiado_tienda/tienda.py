from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre: str, costo_delivery: int) -> None:
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self._productos: list[Producto] = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def costo_delivery(self) -> int:
        return self.__costo_delivery

    def ingresar_producto(self, nombre: str, precio: int, stock: int) -> None:
        nuevo_producto = Producto(nombre, precio, stock)

        if nuevo_producto in self._productos:
            indice = self._productos.index(nuevo_producto)
            self._productos[indice].stock += stock
        else:
            self._productos.append(nuevo_producto)

    @abstractmethod
    def listar_productos(self) -> str:
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto: str, cantidad: int) -> None:
        pass


class Restaurante(Tienda):
    def ingresar_producto(self, nombre: str, precio: int, stock: int) -> None:
        nuevo_producto = Producto(nombre, precio, 0)
        if nuevo_producto not in self._productos:
            self._productos.append(nuevo_producto)

    def listar_productos(self) -> str:
        return "\n".join(f"{p.nombre} - ${p.precio}" for p in self._productos)

    def realizar_venta(self, nombre_producto: str, cantidad: int) -> None:
        pass # Esto no es una buena práctica, sería mejor crear una Interfaz Abstracta

class Supermercado(Tienda):
    def listar_productos(self) -> str:
        lista = []
        for p in self._productos:
            mensaje_stock = f" - Pocos productos disponibles ({p.stock})" if p.stock < 10 else f" - Stock: {p.stock}"
            lista.append(f"{p.nombre} - ${p.precio}{mensaje_stock}")
        return "\n".join(lista)

    def realizar_venta(self, nombre_producto: str, cantidad: int) -> None:
        for p in self._productos:
            if p.nombre.lower() == nombre_producto.lower():
                if cantidad > p.stock:
                    p.stock = 0
                else:
                    p.stock -= cantidad
                return

class Farmacia(Tienda):
    def listar_productos(self) -> str:
        lista = []
        for p in self._productos:
            envio = f" - Envío gratis al solicitar este producto" if p.precio > 15000 else ""
            lista.append(f"{p.nombre} - ${p.precio}{envio}")
        return "\n".join(lista)


    def realizar_venta(self, nombre_producto: str, cantidad: int) -> None:
        if cantidad > 3:
            return
        for p in self._productos:
            if p.nombre.lower() == nombre_producto.lower():
                if cantidad > p.stock:
                    p.stock = 0
                else:
                    p.stock -= cantidad
                return