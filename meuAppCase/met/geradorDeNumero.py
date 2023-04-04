import random

def gerar_numero_aleatorio(pontoAtual):
    if pontoAtual < 30:
        return random.randint(-1, 5)
    elif pontoAtual < 60:
        return random.randint(-3, 5)
    else:
        return random.randint(-5, 3)



