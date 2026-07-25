from typing import Dict, Any, List

inventario = {
    "PRD001": {"nombre": "Monitor 24 pulgadas", "precio": 120000, "stock": 15},
    "PRD002": {"nombre": "Teclado Mecánico", "precio": 45000, "stock": 30},
    "PRD003": {"nombre": "Mouse", "precio": 25000, "stock": 50},
    "PRD004": {"nombre": "Silla Ergonómica", "precio": 150000, "stock": 5},
}

calcular_iva = lambda monto: monto * 0.19
calcular_total_con_iva = lambda monto: monto * 1.19


def buscar_producto(codigo: str) -> Dict[str, Any]:
    # Formato Google
    """Busca un producto en el inventario por su código SKU.

    Args:
        codigo ([str]): Código único identificador del producto (SKU).
    
    Returns:
        [Dict[str, Any]]: Se retorna un diccionario con los datos del producto, o un diccionario vacío si no existe.
    """
    return inventario.get(codigo, {})


def actualizar_stock(codigo: str, cantidad_vendida: int) -> bool:
    # Formato Sphinx
    """Reduce el stock disponible de un producto tras una venta.

    :param codigo: Corresponde al código único del producto.
    :type codigo: [str]
    :param cantidad_vendida: Corresponde a las unidades vendidas.
    :type cantidad_vendida: [int]
    :return: Corresponde a un booleano que indica si la operación fue exitosa.
    :rtype: [bool]
    """
    producto = buscar_producto(codigo)
    if producto and producto["stock"] >= cantidad_vendida:
        producto["stock"] -= cantidad_vendida
        return True
    return False

def generar_resumen_inventario() -> int:
    # Formato Numpy
    """Esta función tiene como objetivo calcular el valor total del inventario.

    Returns
    -------
    [int]
        Retorna la suma del valor (precio * stock) de todos los productos
    """
    valor_total = sum([p["precio"] * p["stock"] for p in inventario.values()])
    return valor_total