class Medicamento:
    IVA: float = 0.19

    def __init__(self, nombre: str, stock: int = 0):
        self.nombre = nombre
        self.stock = stock
        self._precio_bruto: int = 0 #Atributo protegido
        self.precio_final: float = 0.0
        self.descuento: float = 0.0

    @staticmethod
    def validar_mayor_a_cero(numero: int) -> bool:
        return numero > 0

    # Accesador (getter)
    @property
    def precio(self) -> float:
        return self.precio_final

    # Mutador (setter)
    @precio.setter
    def precio(self, precio_bruto: int) -> None:
        if self.validar_mayor_a_cero(precio_bruto):
            self._precio_bruto = precio_bruto # Le asignamos un valor al atributo protegido, por medio de una función setter
            self.precio_final = precio_bruto + (precio_bruto * self.IVA)

            if 10000 <= self.precio_final < 20000:
                self.descuento = 0.1
            elif 20000 <= self.precio_final < 30000:
                self.descuento = 0.2
            elif self.precio_final >= 30000:
                self.descuento = 0.3

            if self.descuento > 0:
                self.precio_final *= (1 - self.descuento)
        else:
            print(f"El precio '{precio_bruto}' no es válido")


    def __eq__(self, otro: object) -> bool:
        if isinstance(otro, Medicamento):
            return self.nombre.lower() == otro.nombre.lower()
        return False

    def __iadd__(self, otro: 'Medicamento') -> 'Medicamento':
        if self == otro:
            self.stock += otro.stock
        return self

    def __str__(self) -> str:
        return f"{self.nombre.upper()} | Stock: {self.stock} | Precio Final: ${self.precio_final:.1f}"


class MedicamentoControlado(Medicamento):
    def __str__(self) -> str:
        return f"RECETA RETENIDA: {super().__str__()}"
        # return f"RECETA RETENIDA: {self.nombre.upper()} | Stock: {self.stock} | Precio Final: ${self.precio_final:.1f}"