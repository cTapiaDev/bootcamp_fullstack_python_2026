from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    def __init__(self, nombre: str, preguntas: list[Pregunta]) -> None:
        self.nombre = nombre
        self.__preguntas = [Pregunta(**p) for p in preguntas]
        self.__listados_respuestas: list[ListadoRespuestas] = []

    @property
    def preguntas(self) -> list[Pregunta]:
        return self.__preguntas

    @property
    def listados_respuestas(self) -> list[ListadoRespuestas]:
        return self.__listados_respuestas

    def mostrar_encuesta(self) -> None:
        print(f"=== Encuesta: {self.nombre} ===")
        for p in self.__preguntas:
            p.mostrar_pregunta()
            print()

    def agregar_listado_respuestas(self, listado: ListadoRespuestas) -> None:
        self.__listados_respuestas.append(listado)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas: list[Pregunta], edad_minima: int, edad_maxima: int) -> None:
        super().__init__(nombre, preguntas)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima

    @property
    def edad_minima(self) -> int:
        return self.__edad_minima

    @edad_minima.setter
    def edad_minima(self, nueva_edad: int) -> None:
        if nueva_edad <= self.__edad_maxima:
            self.__edad_minima = nueva_edad

    @property
    def edad_maxima(self) -> int:
        return self.__edad_maxima

    @edad_maxima.setter
    def edad_maxima(self, nueva_edad: int) -> None:
        if nueva_edad >= self.__edad_minima:
            self.__edad_maxima = nueva_edad

    def agregar_listado_respuestas(self, listado: ListadoRespuestas) -> None:
        if self.__edad_minima <= listado.usuario.edad <= self.__edad_maxima:
            super().agregar_listado_respuestas(listado)
        else:
            print("El usuario no cumple con el rango de edad")

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, preguntas: list[Pregunta], regiones: list[int]) -> None:
        super().__init__(nombre, preguntas)
        self.__regiones = regiones

    @property
    def regiones(self) -> list[int]:
        return self.__regiones

    @regiones.setter
    def regiones(self, nuevas_regiones: list[int]) -> None:
        if nuevas_regiones:
            self.__regiones = nuevas_regiones

    def agregar_listado_respuestas(self, listado: ListadoRespuestas) -> None:
        if listado.usuario.region in self.__regiones:
            super().agregar_listado_respuestas(listado)
        else:
            print("El usuario no pertenece a una región válida")
        