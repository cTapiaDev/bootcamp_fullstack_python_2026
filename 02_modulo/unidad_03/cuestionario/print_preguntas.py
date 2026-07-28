def print_pregunta(enunciado: str, alternativas: list) -> None:
    print(f"{enunciado}\n")
    letras = ['A', 'B', 'C', 'D']
    for i, alt in enumerate(alternativas):
        print(f"{letras[i]}. {alt[0]}")

if __name__ == '__main__':
    pregunta = "¿Cual es la capital de Chile?"
    alternativas = [['Santiago', 1], ['Buenos Aires', 0], ['Lima', 0], ['Bogotá', 0]]
    print_pregunta(pregunta, alternativas)