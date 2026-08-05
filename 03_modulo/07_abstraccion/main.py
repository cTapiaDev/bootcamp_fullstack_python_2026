from entidades import LibroFisico
from ventas import Venta

def main() -> None:
    libro1 = LibroFisico("Clean Code", "Robert C. Martin", 60000)
    libro2 = LibroFisico("Patrones de Diseño", "Gang of Four", 42000)
    libro3 = LibroFisico("Python Fluido", "Liciano Ramalho", 38000)

    # Uso del mutador encapsulado, para modificar por medio de un setter
    libro2.precio = 40000

    # Esto es una función tradicional
    libro2.aplicar_descuento(0.10)

    print("Catálogo:")
    print(libro1)
    print(libro2)
    print(libro3)

    venta_actual = Venta(cliente="Juanito")

    venta_actual.registrar_producto(libro1, 2)
    venta_actual.registrar_producto(libro3, 1)

    venta_actual.imprimir_recibo()

if __name__ == '__main__':
    main()