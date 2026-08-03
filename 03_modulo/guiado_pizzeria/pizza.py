from ingredientes import vegetales, proteicos, masas

class Pizza:
    precio: int = 10000
    tamano: str = 'familiar'
    max_ing: int = 3

    @staticmethod
    def validar_elemento(elemento: str, valores_posibles: list[str]) -> bool:
        return elemento in valores_posibles

    def realizar_pedido(self) -> None:
        self.proteico = input("Ingrese el ingrediente proteico: ").strip().lower()
        self.vegetal_1 = input("Ingrese el primer ingrediente vegetal: ").strip().lower()
        self.vegetal_2 = input("Ingrese el segundo ingrediente vegetal: ").strip().lower()
        self.masa = input("Ingrese el tipo de masa: ").strip().lower()

        es_valido_proteico = self.validar_elemento(self.proteico, proteicos)
        es_valido_v1 = self.validar_elemento(self.vegetal_1, vegetales)
        es_valido_v2 = self.validar_elemento(self.vegetal_2, vegetales)
        es_valido_masa = self.validar_elemento(self.masa, masas)

        self.es_valida: bool = all([es_valido_proteico, es_valido_v1, es_valido_v2, es_valido_masa])
