from abc import ABC, abstractmethod

limpiar_texto = lambda texto: str(texto).strip().upper()

# Interfaz
class IAuditable(ABC):
    @abstractmethod
    def ejecutar_auditoria_codigo(self) -> dict:
        pass


# Clase Abstracta
class EvaluacionBase(ABC):

    def __init__(self, id_entrega: str, nombre_alumno: str, modulo: str):
        self.id_entrega = limpiar_texto(id_entrega)
        self.nombre_alumno = nombre_alumno.title()
        self.modulo = modulo
        self.nota_final: float = 0.0
        self.corregida: bool = False

    def obtener_resumen(self) -> str:
        estado = "Corregida" if self.corregida else "Pendiente"
        return f"[{self.id_entrega}] {self.nombre_alumno} | Módulo: {self.modulo} | Estado: {estado}"

    @abstractmethod
    def corregir_entrega(self) -> float:
        pass