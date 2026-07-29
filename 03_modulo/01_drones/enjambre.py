from dron import Dron
from typing import List

class Enjambre:

    def __init__(self, nombre_flota: str):
        self.nombre_flota = nombre_flota
        self.drones: List[Dron] = []

    def registrar_dron(self, nuevo_dron: Dron) -> None:
        self.drones.append(nuevo_dron)
        print(f"Dron {nuevo_dron.identificador} registrado en la flota '{self.nombre_flota}'")

    def reporte_general(self) -> None:
        print(f"\n=== ESTADO DEL ENJAMBRE: {self.nombre_flota} ===")
        if not self.drones:
            print("No hay drones registrados.")
            return

        for dron in self.drones:
            bateria_str = f"{dron.bateria.carga_actual}"
            print(f"ID: {dron.identificador} | Estado: {dron.estado} | Batería: {bateria_str} | Distancia Total: {dron.distancia_recorrida} km")
        print("=" * 20)

    def despliegue_masivo(self, distancia: int, peso: int) -> None:
        print(f"\nIniciando despliegue masivo ({distancia} km, {peso} kg)...")
        for dron in self.drones:
            if dron.estado == "EN BASE":
                dron.volar(distancia, peso)