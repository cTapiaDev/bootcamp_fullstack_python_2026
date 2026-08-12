from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, requerida: bool, alternativas: list[Alternativa], ayuda: str = ""):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.__alternativas = [Alternativa(**alt) for alt in alternativas]

    @property
    def alternativas(self) -> list[Alternativa]:
        return self.__alternativas

    def mostrar_pregunta(self) -> None:
        req = "(Requerida)" if self.requerida else "(Opcional)"
        print(f"Pregunta: {self.enunciado} {req}")
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")
        for alt in self.__alternativas:
            alt.mostrar_alternativa()