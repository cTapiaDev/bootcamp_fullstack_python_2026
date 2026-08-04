class OrdenCompra:

    def nueva_orden(self, identificador: int) -> None:
        self.identificador = identificador
        self.total_productos = 0
        self.monto = 0
        self.codigo_descuento = ''

    def asignar_monto(self, nuevo_monto: int) -> None:
        self.monto = nuevo_monto
        self.codigo_descuento = ''

        if self.monto > 20000:
            self.codigo_descuento = '20PORCIENTO'
        elif self.monto > 10000:
            self.codigo_descuento = '10PORCIENTO'

    def __str__(self) -> str:
        desc = f" (Descuento: {self.codigo_descuento})" if self.codigo_descuento else ""
        return f"Orden #{self.identificador} | Monto: ${self.monto}{desc}"