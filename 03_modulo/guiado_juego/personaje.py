class Personaje:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self) -> str:
        return f"NOMBRE: {self.nombre}   NIVEL: {self.nivel}   EXP: {self.experiencia}"

    @estado.setter
    def estado(self, exp_recibida: int) -> None:
        exp_temporal = self.experiencia + exp_recibida

        while exp_temporal >= 100:
            self.nivel += 1
            exp_temporal -= 100

        while exp_temporal < 0:
            if self.nivel > 1:
                self.nivel -= 1
                exp_temporal += 100
            else:
                exp_temporal = 0
                break

        self.experiencia = exp_temporal

    __lt__ = lambda self, otro: self.nivel < otro.nivel
    __gt__ = lambda self, otro: self.nivel > otro.nivel
    __eq__ = lambda self, otro: self.nivel == otro.nivel

    def probabilidad_ganar(self, otro: 'Personaje') -> float:
        if self < otro:
            return 0.33
        elif self > otro:
            return 0.66
        else:
            return 0.50

    @staticmethod
    def mostrar_dialogo(probabilidad: float) -> str:
        print(f"\nCon tu nivel actual, tienes {probabilidad * 100}% de probabilidades de ganarle al Orco.")
        print("\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        return input("\n¿Qué deseas hacer?\n1. Atacar\n2. Huir\n").strip()