class DimensionError(Exception):
    def __init__(self, mensaje: str, dimension: int = None, maximo: int = None) -> None:
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo


    def __str__(self) -> str:
        if self.dimension is None and self.maximo is None:
            return super().__str__()

        retorno = self.mensaje
        if self.dimension is not None:
            retorno += f" Dimensión recibida: {self.dimension}"
        if self.maximo is not None:
            retorno += f" Máximo permitido: {self.maximo}"

        return retorno

        