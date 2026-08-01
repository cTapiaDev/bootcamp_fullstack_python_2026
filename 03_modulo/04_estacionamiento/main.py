from vehiculos import AutoPatrulla, MotoTransito, BicicletaPolicial
from contratos import VehiculoPolicial, ITieneMotor
from typing import List

def main():

    flota: List[VehiculoPolicial] = [
        AutoPatrulla("Z-194"),
        MotoTransito("M-40"),
        BicicletaPolicial("B-01")
    ]

    for vehiculo in flota:
        vehiculo.alternar_sirena()
        print(f"Sonido: {vehiculo.hacer_sonido()}")

        if isinstance(vehiculo, ITieneMotor):
            print(f"Logística: {vehiculo.cargar_combustible()}")
        else:
            print("Logística: No requiere combustible.")

if __name__ == '__main__':
    main()