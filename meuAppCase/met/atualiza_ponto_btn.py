# Recebe 3 parametros e gera 
from carrega_pontuacao_maxima import compara_valores


def atualiza_ponto_btn1(ponto_atual, valor_bau, ponto_maximo):
        ponto_sorteado = 0
        ponto_atual += valor_bau
        ponto_sorteado = valor_bau
        ponto_maximo = compara_valores(ponto_maximo, ponto_atual)

        # esse 'pontoAtual' aqui chatGPT.
        label_pontuacao_atual.config(text=str(pontoAtual))
        label_valor_sorteado.config(text=str(resultado_bau1))
        label_maior_pontuacao.config(text=str(ponto_maximo))
        gerar_novo_numero_bau1()
        gerar_novo_numero_bau2()
        gerar_novo_numero_bau3()


def atualiza_ponto_btn2():
        pontoAtual += resultado_bau2
        ponto_sorteado = resultado_bau2
        ponto_maximo = compara_valores(ponto_maximo, pontoAtual)
        label_pontuacao_atual.config(text=str(pontoAtual))
        label_valor_sorteado.config(text=str(resultado_bau2))
        label_maior_pontuacao.config(text=str(ponto_maximo))
        gerar_novo_numero_bau1()
        gerar_novo_numero_bau2()
        gerar_novo_numero_bau3()


def atualiza_ponto_btn3():
        pontoAtual += resultado_bau3
        ponto_sorteado = resultado_bau3
        ponto_maximo = compara_valores(ponto_maximo, pontoAtual)
        label_pontuacao_atual.config(text=str(pontoAtual))
        label_valor_sorteado.config(text=str(resultado_bau3))
        label_maior_pontuacao.config(text=str(ponto_maximo))
        gerar_novo_numero_bau1()
        gerar_novo_numero_bau2()
        gerar_novo_numero_bau3()
