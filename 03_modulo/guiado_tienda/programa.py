from tienda import Restaurante, Supermercado, Farmacia

def main() -> None:
    print("1. Restaurante\n2. Supermercado\n3. Farmacia")
    tipo_tienda = input("Ingrese el tipo de tienda: ").strip()

    nombre_tienda = input("Ingrese el nombre de la tienda: ").strip()
    costo_delivery = int(input("Ingrese el costo de delivery: "))

    if tipo_tienda == '1':
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda == '2':
        tienda = Supermercado(nombre_tienda, costo_delivery)
    else:
        tienda = Farmacia(nombre_tienda, costo_delivery)

    while True:
        opcion_ingreso = input("¿Desea ingresar un producto? (s/n): ").strip().lower()
        if opcion_ingreso != 's':
            break

        nombre_prod = input("Nombre del producto: ").strip()
        precio_prod = int(input("Precio: "))
        stock_prod = int(input("Stock: "))
        tienda.ingresar_producto(nombre_prod, precio_prod, stock_prod)

    while True:
        print("\n--- Menú ---")
        print("1. Listar productos")
        print("2. Realizar una venta")
        print("3. Salir")
        opcion_menu = input("Seleccione una acción: ").strip()

        if opcion_menu == '1':
            print("\n" + tienda.listar_productos())
        elif opcion_menu == '2':
            nombre_venta = input("Ingrese el nombre del producto a vender: ").strip()
            cantidad_venta = int(input("Ingrese la cantidad requerida: "))
            tienda.realizar_venta(nombre_venta, cantidad_venta)
            print("Venta procesada!")
        elif opcion_menu == '3':
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()