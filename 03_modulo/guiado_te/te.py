class Te:

    duracion: int = 365

    @staticmethod
    def obtener_tiempo_recomendacion(sabor: int) -> tuple:
        datos_sabor = {
            1: (3, 'Se recomienda consumir al desayuno'),
            2: (5, 'Se recomienda consumir al medio día'),
            3: (6, 'Se recomienda consumir al atardecer'),
        }

        return datos_sabor.get(sabor, (0, 'Recomendación no disponible'))

    @staticmethod
    def obtener_precio(formato: int) -> int:
        precios = {
            300: 3000,
            500: 5000
        }

        return precios.get(formato, 0)