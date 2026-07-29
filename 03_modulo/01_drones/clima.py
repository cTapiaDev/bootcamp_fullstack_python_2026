import random

formatear_alerta = lambda mensaje: f"ALERTA CLIMÁTICA: {mensaje}"

class Clima:
    # Atributo de Clase (Estático)
    viento_maximo_permitido: int = 40

    # Decorador @staticmethod -> Le dice al script que esto es un método estático.
    # Estos no utilizan 'self' porque no modifica ni lee el estado de un objeto.
    @staticmethod
    def generar_viento_actual() -> int:
        return random.randint(0, 60)

    @staticmethod
    def es_seguro_volar(velocidad_viento: int) -> bool:
        if velocidad_viento > Clima.viento_maximo_permitido:
            print(formatear_alerta(f"Viento a {velocidad_viento} km/h. Vuelos suspendidos."))
            return False
        return True