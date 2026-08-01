from abc import ABC, abstractmethod

class ICondecorable(ABC):
    @abstractmethod
    def recibir_medalla(self) -> str:
        pass

class Soldado(ABC):
    def __init__(self, nombre: str, rango: str):
        self.nombre = nombre
        self.rango = rango

    def reportarse(self) -> str:
        return f"[{self.rango.upper()}] {self.nombre.title()}"

    @abstractmethod
    def saludar(self) -> str:
        pass