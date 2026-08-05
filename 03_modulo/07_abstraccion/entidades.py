from abc import ABC, abstractmethod

formatear_moneda = lambda valor: f"${valor:,.0f}".replace(',', '.')

class IProducto(ABC):
    @abstractmethod
    def aplicar_descuento(self, porcentaje: float) -> None:
        pass

class LibroFisico(IProducto):
    def __init__(self, titulo: str, autor: str, precio: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio # Atributo privado, doble __

    @property
    def precio(self) -> int:
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio: int) -> None:
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo o cero.")

    def aplicar_descuento(self, porcentaje: float) -> None:
        if 0 < porcentaje < 1:
            self.__precio = int(self.__precio * (1 - porcentaje))

    def __str__(self) -> str:
        return f"Libro: {self.titulo} ({self.autor}) | {formatear_moneda(self.precio)}"