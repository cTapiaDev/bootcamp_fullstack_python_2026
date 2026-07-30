from te import Te

def main():
    print("=== SISTEMA DE PEDIDOS DE TE ===")
    print("Opciones de sabor: 1 (Té negro) | 2 (Té verde) | 3 (Agua de hierbas)")

    sabor_ingresado = int(input("Ingrese el número del sabor que desea: "))
    formato_ingresado = int(input("Ingrese el formato que desea (300 o 500): "))

    diccionario_nombres = {
        1: "Té negro",
        2: "Té verde",
        3: "Agua de hierbas"
    }
    nombre_sabor = diccionario_nombres.get(sabor_ingresado, "Sabor desconocido")
    precio = Te.obtener_precio(formato_ingresado)
    tiempo, recomendacion = Te.obtener_tiempo_recomendacion(sabor_ingresado)


    print("\n=== DETALLE DEL PEDIDO ===")
    print(f"Sabor del té: {nombre_sabor}")
    print(f"Formato: {formato_ingresado} gr")
    print(f"Precio: ${precio}")
    print(f"Tiempo de preparación: {tiempo} minutos")
    print(f"Recomendación: {recomendacion}")

if __name__ == '__main__':
    main()