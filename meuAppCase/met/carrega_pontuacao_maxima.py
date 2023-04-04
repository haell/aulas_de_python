# Verificar se um número é maior que o outro, caso seja maior então substituir, se não, manter o valor.


def compara_valores(primeiro_numero, segundo_numero):
    if segundo_numero > primeiro_numero:
        primeiro_numero = segundo_numero
    return primeiro_numero
