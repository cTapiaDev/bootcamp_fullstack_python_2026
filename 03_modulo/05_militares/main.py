from soldados import SargentoVeterano, ReclutaNovato, Francotirador
from contratos import Soldado, ICondecorable
from typing import List

def main():

    peloton: List[Soldado] = [
        SargentoVeterano("cortés"),
        ReclutaNovato("pinto"),
        Francotirador("ghost")
    ]

    for soldado in peloton:
        print(f"\nSe acerca a: {soldado.reportarse()}")
        print(f"Respuesta: {soldado.saludar()}")

        if isinstance(soldado, ICondecorable):
            print("Ceremonia: Se le otorga una medalla")
            print(f"{soldado.recibir_medalla()}")
        else:
            print("No recibe medalla")

if __name__ == '__main__':
    main()