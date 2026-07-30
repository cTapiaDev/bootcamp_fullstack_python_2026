from ticket import Ticket
from algoritmo import AlgoritmoPrecios
from typing import List

calcular_ocupacion = lambda vendidos, total: vendidos / total

class Evento:

    comision_plataforma: float = 0.05

    def __init__(self, nombre: str, capacidad_maxima: int, precio_inicial: int):
        self.nombre = nombre
        self.capacidad_maxima = capacidad_maxima
        self.precio_actual = precio_inicial
        self.entradas_vendidas: List[Ticket] = []
        self.recaudacion_total = 0

    def procesar_compra(self, nombre_comprador: str) -> bool:
        if len(self.entradas_vendidas) >= self.capacidad_maxima:
            print("SOLD OUT: No quedan entradas disponibles.")
            return False

        nuevo_ticket = Ticket(nombre_comprador, self.precio_actual)
        self.entradas_vendidas.append(nuevo_ticket)

        self.recaudacion_total += self.precio_actual
        print(f"Compra exitosa. Ticket [{nuevo_ticket.id_ticket}] emitido a {nombre_comprador} por ${self.precio_actual}.")

        ocupacion = calcular_ocupacion(len(self.entradas_vendidas), self.capacidad_maxima)
        self.precio_actual = AlgoritmoPrecios.calcular_nuevo_precio(self.precio_actual, ocupacion)

        return True

    def calcular_ganancias_netas(self) -> int:
        descuento = self.recaudacion_total * Evento.comision_plataforma
        return int(self.recaudacion_total - descuento)