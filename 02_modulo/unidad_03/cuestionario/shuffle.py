import random

def shuffle_alt(pregunta: dict) -> list:
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    return alternativas

if __name__ == '__main__':
    import datos as d
    print(shuffle_alt(d.pool_preguntas['basicas']['pregunta_1']))