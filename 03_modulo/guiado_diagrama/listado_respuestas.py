class ListadoRespuestas:
    def __init__(self, usuario, respuestas: list[int]) -> None:
        self.__usuario = usuario
        self.__respuestas = respuestas

    @property
    def usuario(self):
        return self.__usuario

    @property
    def respuestas(self) -> list[int]:
        return self.__respuestas