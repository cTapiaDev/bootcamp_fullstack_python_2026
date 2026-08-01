from contratos import VehiculoPolicial, ITieneMotor

class AutoPatrulla(VehiculoPolicial, ITieneMotor):
    def hacer_sonido(self) -> str:
        return "¡WEE-WOO WEE-WOO! (Sonido Fuerte)"

    def cargar_combustible(self) -> str:
        return "Llenando estanque con combustible de 95"

class MotoTransito(VehiculoPolicial, ITieneMotor):
    def hacer_sonido(self) -> str:
        return "¡WEEE-WEEE-WEEE! (Sonido agudo)"
    
    def cargar_combustible(self) -> str:
        return "Llenando estanque pequeño"

class BicicletaPolicial(VehiculoPolicial):
    def hacer_sonido(self) -> str:
        return "¡Ring Ring!"