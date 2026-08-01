from abc import ABC, abstractmethod

formatear_estado = lambda estado: "ENCENDIDA" if estado else "APAGADA"

# Interfaz
class ITieneMotor(ABC):
    @abstractmethod
    def cargar_combustible(self) -> str:
        pass

# Clase Abstracta
class VehiculoPolicial(ABC):
    def __init__(self, identificador: str):
        self.identificador = identificador
        self.sirena_encendida = False

    def alternar_sirena(self) -> None:
        self.sirena_encendida = not self.sirena_encendida # not False = True | not True = False
        print(f"[{self.identificador}] Sirena {formatear_estado(self.sirena_encendida)}")

    @abstractmethod
    def hacer_sonido(self) -> str:
        pass