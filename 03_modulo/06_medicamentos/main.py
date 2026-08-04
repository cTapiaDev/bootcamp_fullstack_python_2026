from medicamento import Medicamento, MedicamentoControlado
from orden_compra import OrdenCompra

def main() -> None:
    inventario: list[Medicamento] = []

    while True:
        try:
            opcion = int(input("¿Desea agregar un medicamento?\n1. Sí\n2. No\n> "))
        except ValueError:
            print("Entrada inválida")
            continue

        if opcion != 1:
            break

        nombre = input("Ingrese nombre del medicamento: ").strip()

        try:
            stock = int(input("Ingrese stock inicial: "))
            es_controlado = input("¿Es controlado? (s/n): ").strip().lower == 's'

            nuevo_med = MedicamentoControlado(nombre, stock) if es_controlado else Medicamento(nombre, stock)

            if nuevo_med in inventario:
                indice = inventario.index(nuevo_med)
                inventario[indice] += nuevo_med #Esto invoca el método __iadd__
                print(f"Stock sumado al medicamento existente: {inventario[indice].nombre}")

            else:
                precio_base = int(input("Ingrese precio bruto: "))
                nuevo_med.precio = precio_base #Asignación que desencadena el mutador (@setter)
                inventario.append(nuevo_med)

        except ValueError:
            print("Error: Ingrese valores numéricos válidos")

    print("\n--- RESUMEN DE INVENTARIO ---")
    for med in inventario:
        print(med)
    print(f"\nTotal de ítems únicos: {len(inventario)}")

    print("\n--- GENERACIÓN DE ORDEN DE COMPRA ---")
    orden = OrdenCompra()
    orden.nueva_orden(112233)

    try:
        monto_compra = int(input("Ingrese el monto total de la compra: "))
        orden.asignar_monto(monto_compra)
        print(f"\n{orden}")
    except ValueError:
        print("Monto inválido")

if __name__ == "__main__":
    main()