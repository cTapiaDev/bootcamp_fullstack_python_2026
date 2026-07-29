from bateria import Bateria

calcular_consumo = lambda distancia, peso: (distancia * 2) + peso

class Dron:

    peso_maximo_carga: int = 5

    def __init__(self, identificador: str):
        self.identificador = identificador
        self.estado = 'EN BASE'
        self.distancia_recorrida = 0
        self.bateria = Bateria(capacidad_maxima=100) # Instancia de Bateria (Creación del Objeto Bateria)


    def volar(self, distancia: int, peso_carga: int) -> None:
        if peso_carga > Dron.peso_maximo_carga:
            print(f"[{self.identificador}] Carga excede el limite de {Dron.peso_maximo_carga} kg.")

        if self.estado == "SIN BATERIA":
            print(f"[{self.identificador}] No puede volar. Requiere recarga inmediata.")
            return

        consumo_energia = calcular_consumo(distancia, peso_carga)

        if self.bateria.consumir(consumo_energia):
            self.estado = "VOLANDO"
            self.distancia_recorrida += distancia
            print(f"[{self.identificador}] Vuelo exitoso de {distancia} km. Batería restante: {self.bateria.carga_actual}")
            self.estado = "EN BASE"
        else:
            self.estado = "SIN BATERIA"
            print(f"[{self.identificador}] Vuelo fallido por falta de energía.")

    def reparar(self) -> None:
        self.bateria.recargar()
        self.estado = "EN BASE"
        print(f"[{self.identificador}] Mantenimiento completado.")

    