

class Bateria():

    # Método Constructor: Inicializa los atributos de un objeto en una instancia.
    def __init__(self, capacidad_maxima: int):
        # Atributos de Instancia
        self.capacidad_maxima = capacidad_maxima
        self.carga_actual = capacidad_maxima
        self.en_buen_estado = True

    # Métodos de Instancia
    # Modifica el estado del objeto a través de 'self'
    def consumir(self, cantidad: int) -> bool:
        if not self.en_buen_estado:
            print("Batería dañada.")
            return False

        if self.carga_actual >= cantidad:
            self.carga_actual -= cantidad
            return True
        else:
            self.carga_actual = 0
            return False

    def recargar(self) -> None:
        self.carga_actual = self.capacidad_maxima
        print("Batería recargada al 100%")