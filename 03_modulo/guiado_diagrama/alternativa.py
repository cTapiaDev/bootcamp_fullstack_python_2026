class Alternativa:
    def __init__(self, contenido: str, ayuda: str = "") -> None:
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self) -> None:
        if self.ayuda:
            print(f"  * {self.contenido} (Ayuda: {self.ayuda})")
        else:
            print(f"  * {self.contenido}")