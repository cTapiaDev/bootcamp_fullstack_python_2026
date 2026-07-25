import ventas
import ux as interfaz
from base_datos import generar_resumen_inventario
from sys import exit

def iniciar_caja() -> None:
    carrito_actual = []

    while True:
        interfaz.mostrar_encabezado("CAJA REGISTRADORA")
        print("1. Agregar producto al carrito")
        print("2. Procesar venta")
        print("3. Ver valor total del inventario")
        print("4. Cerrar")

        opcion = input("\nSeleccione una acción: ").strip()

        if opcion == '1':
            codigo = input("Ingrese SKU del producto (ej. PRD001): ").strip().upper()
            cant_str = input("Ingrese cantidad: ").strip()

            if cant_str.isnumeric():
                ventas.agregar_al_carrito(carrito_actual, codigo, int(cant_str))
            else:
                print("Error: La cantidad debe ser numérica.")
                interfaz.pausar(1)

        elif opcion == '2':
            exito = ventas.procesar_pago(carrito_actual)
            if exito:
                carrito_actual.clear()

        elif opcion == '3':
            interfaz.limpiar_pantalla()
            valor = generar_resumen_inventario()
            print(f"El valor total del inventario en bodega es: ${valor:,.0f}")
            input("\nPresione Enter para volver...")

        elif opcion == '4':
            print("Cerrando sesión...")
            interfaz.animacion_procesando("Sincronizando con servidor...")
            exit()

        else:
            print("Opción no válida.")
            interfaz.pausar(1)

if __name__ == '__main__':
    iniciar_caja()