from listado_respuestas import ListadoRespuestas
from encuesta import Encuesta

class Usuario:
    def __init__(self, correo: str, edad: int, region: int) -> None:
        self.__correo = correo
        self.__edad = edad
        self.__region

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo: str) -> None:
        self.__correo = nuevo_correo

    @property
    def edad(self) -> int:
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad: int) -> None:
        self.__edad = nueva_edad

    @property
    def region(self) -> int:
        return self.__region
        
    @region.setter
    def region(self, nueva_region: int) -> None:
        self.__region = nueva_region

    def contestar_encuesta(self, encuesta: Encuesta, respuestas: list[int]) -> None:
        nuevo_listado = ListadoRespuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(nuevo_listado)