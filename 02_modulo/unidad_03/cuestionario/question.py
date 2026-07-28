import random
from shuffle import shuffle_alt
import datos as d

def choose_q(dificultad: str) -> tuple:
    preguntas_disponibles = list(d.pool_preguntas[dificultad].keys())

    elegida = random.choice(preguntas_disponibles)
    pregunta = d.pool_preguntas[dificultad].pop(elegida)

    enunciado = pregunta['enunciado']
    alternativas_mezcladas = shuffle_alt(pregunta)

    return enunciado, alternativas_mezcladas

if __name__ == '__main__':
    pregunta, alternativas = choose_q('basicas')
    print(f"El enunciado es: {pregunta}")
    print(f"Las alternativas son: {alternativas}")