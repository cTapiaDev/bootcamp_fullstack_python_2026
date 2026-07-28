obtener_indice = lambda eleccion: ['a', 'b', 'c', 'd'].index(eleccion)

def verificar(alternativas: list, eleccion: str) -> bool:
    idx = obtener_indice(eleccion)

    if alternativas[idx][1] == 1:
        print('Respuesta Correcta')
        return True
    else:
        print('Respuesta Incorrecta')
        return False

if __name__ == '__main__':
    alts = [['Falso', 0], ['Falso', 0], ['Verdadero', 1], ['Falso', 0]]
    elec = 'c'
    verificar(alts, elec)