import base_datos
import ux

def agregar_al_carrito(carrito: list, codigo: str, cantidad: int) -> None:
    producto = base_datos.buscar_producto(codigo)

    if not producto:
        print("Error: Producto no encontrado")
        ux.pausar(1.5)
        return

    if producto["stock"] < cantidad:
        print(f"Error: Stock insuficiente. Stock actual: {producto['stock']}")
        ux.pausar(1.5)
        return

    subtotal = producto["precio"] * cantidad
    carrito.append({
        "codigo": codigo,
        "nombre": producto["nombre"],
        "cantidad": cantidad,
        "precio_unitario": producto["precio"],
        "subtotal": subtotal
    })
    print(f"{cantidad}x {producto["nombre"]} agregado(s) al carrito.")
    ux.pausar(1)



def procesar_pago(carrito: list) -> bool:
    if not carrito:
        print("El carrito está vacío.")
        ux.pausar(1)
        return

    subtotal_neto = sum([item["subtotal"] for item in carrito])
    iva = base_datos.calcular_iva(subtotal_neto)
    total = base_datos.calcular_total_con_iva(subtotal_neto)

    ux.mostrar_encabezado("RESUMEN DE VENTA")
    for item in carrito:
        print(f"{item['cantidad']}x {item['nombre']} - ${item['subtotal']}")

    print("-" * 50)
    print(f"Neto   : ${subtotal_neto:,.0f}")
    print(f"IVA    : ${iva:,.0f}")
    print(f"TOTAL  : ${total:,.0f}")

    confirmacion = input("\n¿Confirmar pago? (s/n): ").strip().lower()
    if confirmacion == 's':
        ux.animacion_procesando("Procesando pago con tarjeta")

        for item in carrito:
            base_datos.actualizar_stock(item['codigo'], item['cantidad'])

        print("VENTA APROBADA. Imprimiendo comprobante...")
        ux.pausar(2)
        return True
    else:
        print("Venta cancelada...")
        ux.pausar(1)
        return False