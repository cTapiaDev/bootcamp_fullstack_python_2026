# Parámetros Obligatorios
def extremo_multiplicado(lista, factor):
    minimo = min(lista)
    maximo = max(lista)
    return factor * minimo, factor * maximo

# print(extremo_multiplicado(4, [1, 2, 3, 4]))
print(extremo_multiplicado([1, 2, 3, 4], 4))
print(extremo_multiplicado(factor=4, lista=[1, 2, 3, 4]))



# Parámetros Opcionales o por Defecto
def elevar(base, exponente, redondear=False):
    if redondear:
        valor = round(base**exponente, 2)
    else:
        valor = base**exponente
    return valor

print(f"\nSin redondear: {elevar(2.5, 3)}")
print(f"Redondeado: {elevar(2.5, 3, True)}")


def aplicar_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    return precio - descuento

print(f"Descuento por defecto: {aplicar_descuento(5000)}")
print(f"Descuento personalizado: {aplicar_descuento(5000, 25)}")