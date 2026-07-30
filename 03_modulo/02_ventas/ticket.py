import uuid

generar_id_unico = lambda: str(uuid.uuid4())[:8].upper()

class Ticket:

    def __init__(self, nombre_comprador: str, precio_pagado: int):
        self.id_ticket = generar_id_unico()
        self.nombre_comprador = nombre_comprador
        self.precio_pagado = precio_pagado
        self.es_valido = True

    def anular_entrada(self) -> None:
        if self.es_valido:
            self.es_valido = False
            print(f"Ticket {self.id_ticket} anulado correctamente.")
        else:
            print(f"El ticket ya fue anulado.")