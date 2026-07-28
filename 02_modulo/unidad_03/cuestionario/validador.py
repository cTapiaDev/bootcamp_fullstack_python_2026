def validate(opciones: list, eleccion: str) -> str:
    while eleccion not in opciones:
        eleccion = input('Opción no válida, ingrese una de las opciones válidas: ').strip().lower()
    return eleccion

if __name__ == '__main__':
    eleccion = input("Ingresa una opción: ").strip().lower()
    letras = ['a', 'b', 'c', 'd']
    print(validate(letras, eleccion))