from contratos import Soldado, ICondecorable

class ReclutaNovato(Soldado):
    def __init__(self, nombre: str):
        super().__init__(nombre, "Recluta")

    def saludar(self) -> str:
        return "¡SEÑOR, SI SEÑOR!"

class SargentoVeterano(Soldado, ICondecorable):
    def __init__(self, nombre: str):
        super().__init__(nombre, "Sargento")

    def saludar(self) -> str:
        return "Todo en orden en el cuartel, mi General"

    def recibir_medalla(self) -> str:
        return "Medalla de Sargento recibida"

class Francotirador(Soldado, ICondecorable):
    def __init__(self, nombre: str):
        super().__init__(nombre, "Especialista")

    def saludar(self) -> str:
        return "¡Firme!"

    def recibir_medalla(self) -> str:
        return "Medalla de Especialista"