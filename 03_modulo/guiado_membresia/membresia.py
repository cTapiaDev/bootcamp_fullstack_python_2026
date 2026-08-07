from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo_electronico: str, numero_tarjeta: str) -> None:
        self.correo_electronico = correo_electronico
        self.numero_tarjeta = numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, tipo: int) -> 'Membresia':
        pass

    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)    
        elif tipo == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)            
        elif tipo == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)          
        elif tipo == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
        else:
            return Gratis(self.correo_electronico, self.numero_tarjeta)

class Gratis(Membresia):
    costo: int = 0
    max_dispositivos: int = 1

    def cambiar_suscripcion(self, tipo: int) -> Membresia:
        if 1 <= tipo <= 4:
            return self._crear_nueva_membresia(tipo)
        return self

class Basica(Membresia):
    costo: int = 3000
    max_dispositivos: int = 2

    def __init__(self, correo_electronico: str, numero_tarjeta: str) -> None:
        super().__init__(correo_electronico, numero_tarjeta)

        if isinstance(self, Pro):
            self.dias_regalo = 15
        elif isinstance(self, (Familiar, SinConexion)):
            self.dias_regalo = 7

    def cambiar_suscripcion(self, tipo: int) -> Membresia:
        if 2 <= tipo <= 4:
            return self._crear_nueva_membresia(tipo)
        return self

    cancelar_suscripcion = lambda self: Gratis(self.correo_electronico, self.numero_tarjeta)

class Familiar(Basica):
    costo: int = 5000
    max_dispositivos: int = 5

    modificar_control_parental = lambda self: None

    def cambiar_suscripcion(self, tipo: int) -> Membresia:
        if tipo in [1, 3, 4]:
            return self._crear_nueva_membresia(tipo)
        return self

class SinConexion(Basica):
    costo: int = 3500
    max_dispositivos: int = 2

    incrementar_contenido = lambda self: None

    def cambiar_suscripcion(self, tipo: int) -> Membresia:
        if tipo in [1, 2, 4]:
            return self._crear_nueva_membresia(tipo)
        return self

class Pro(Familiar, SinConexion):
    costo: int = 7000
    max_dispositivos: int = 6

    def cambiar_suscripcion(self, tipo: int) -> Membresia:
        if 1 <= tipo <= 3:
            return self._crear_nueva_membresia(tipo)
        return self