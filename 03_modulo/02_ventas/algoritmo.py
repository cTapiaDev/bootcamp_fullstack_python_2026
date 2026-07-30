class AlgoritmoPrecios:

    multiplicador_base: float = 1.15

    @staticmethod
    def calcular_nuevo_precio(precio_actual: int, porcentaje_ocupacion: float) -> int:
        if porcentaje_ocupacion >= 0.8:
            return int(precio_actual * AlgoritmoPrecios.multiplicador_base * 1.5)
        elif porcentaje_ocupacion >= 0.5:
            return int(precio_actual * AlgoritmoPrecios.multiplicador_base)

        return precio_actual