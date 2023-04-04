#encoding: utf-8
import sys
sys.path.append('D:\GitHub\\aulas_de_python\meuAppCase\met')

from geradorDeNumero  import  gerar_numero_aleatorio as gna
from carrega_pontuacao_maxima import compara_valores
#from atualiza_ponto_btn import atualiza_ponto_btn1, atualiza_ponto_btn2, atualiza_ponto_btn3

import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        master.title("Caça Baú!")
        master.geometry("650x450")
        
        self.pontoAtual = 0
        self.ponto_sorteado = 0

        self.ponto_maximo = 0
        
        self.resultado_bau1 = gna(self.pontoAtual)
        self.resultado_bau2 = gna(self.pontoAtual)
        self.resultado_bau3 = gna(self.pontoAtual)
        

        self.label_maior_pontuacao_nome = tk.Label(
            master, text="Ponto_maximo", font=("Arial", 10, "bold"), background="green", fg="white")
        self.label_maior_pontuacao_nome.grid(row=0, column=0, columnspan=1, padx=12, sticky="NESW")

        self.label_maior_pontuacao = tk.Label(
            master, text=str(self.ponto_maximo), font=("Arial", 12), bd=4, relief="sunken", highlightbackground="green", highlightthickness=2)
        self.label_maior_pontuacao.grid(row=0, column=1, padx=5, columnspan=1, sticky="NESW")

        self.label_jogador_rotulo = tk.Label(
            master, text="Jogador: ", font=("Arial", 10, "bold"))
        self.label_jogador_rotulo.grid(row=1, column=0, padx=12)

        self.label_jogador_email = tk.Label(
            master, text="jogador@gmail.com", font=("Arial", 14), pady=10, fg="blue")
        self.label_jogador_email.grid(row=1, column=1, columnspan=2, sticky=tk.W)

        self.label_pontuacao_atual_nome = tk.Label(
            master, text="Pontuação atual", font=("Arial", 12))
        self.label_pontuacao_atual_nome.grid(row=2, column=1)

        self.label_pontuacao_atual = tk.Label(
            master, text=str(self.pontoAtual), font=("Arial", 48), padx=10)
        self.label_pontuacao_atual.grid(row=3, column=1)        


        def gerar_novo_numero_bau1():
            self.resultado_bau1 = gna(self.pontoAtual)
            #self.bau1.config(text=self.resultado_bau1)
        
        def gerar_novo_numero_bau2():
            self.resultado_bau2 = gna(self.pontoAtual)
            #self.bau2.config(text=self.resultado_bau2)
        
        def gerar_novo_numero_bau3():
            self.resultado_bau3 = gna(self.pontoAtual)
            #self.bau3.config(text=self.resultado_bau3)

        def atualiza_ponto_btn1():
            self.pontoAtual += self.resultado_bau1
            self.ponto_sorteado = self.resultado_bau1
            self.ponto_maximo = compara_valores(self.ponto_maximo, self.pontoAtual)
            self.label_pontuacao_atual.config(text=str(self.pontoAtual)) # esse 'pontoAtual' aqui chatGPT.
            self.label_valor_sorteado.config(text=str(self.resultado_bau1))            
            self.label_maior_pontuacao.config(text=str(self.ponto_maximo))         
            gerar_novo_numero_bau1()            
            gerar_novo_numero_bau2()            
            gerar_novo_numero_bau3()
            
                        
                                

        def atualiza_ponto_btn2():
            self.pontoAtual += self.resultado_bau2
            self.ponto_sorteado = self.resultado_bau2
            self.ponto_maximo = compara_valores(self.ponto_maximo, self.pontoAtual)
            self.label_pontuacao_atual.config(text=str(self.pontoAtual))
            self.label_valor_sorteado.config(text=str(self.resultado_bau2))         
            self.label_maior_pontuacao.config(text=str(self.ponto_maximo))
            gerar_novo_numero_bau1()
            gerar_novo_numero_bau2()
            gerar_novo_numero_bau3()          
                               

            

        def atualiza_ponto_btn3():
            self.pontoAtual += self.resultado_bau3
            self.ponto_sorteado = self.resultado_bau3
            self.ponto_maximo = compara_valores(self.ponto_maximo, self.pontoAtual)
            self.label_pontuacao_atual.config(text=str(self.pontoAtual))
            self.label_valor_sorteado.config(text=str(self.resultado_bau3))            
            self.label_maior_pontuacao.config(text=str(self.ponto_maximo))
            gerar_novo_numero_bau1()
            gerar_novo_numero_bau2()
            gerar_novo_numero_bau3()
                               

            
        self.img = tk.PhotoImage(file="D:\GitHub\\aulas_de_python\meuAppCase\met\img\\bau.png")
        
        self.label_valor_sorteado_nome = tk.Label(
            master, text="Valor sorteado: ", font=("Arial", 12))
        self.label_valor_sorteado_nome.grid(row=6, column=0, columnspan=2, padx=10, sticky="NESW")

        self.label_valor_sorteado = tk.Label(
            master, text=str(self.ponto_sorteado), font=("Arial", 22), padx=10, bd=4, relief="flat", highlightbackground="Gray", highlightthickness=1)
        self.label_valor_sorteado.grid(row=6, column=1, pady=20) 

        trunk_one = tk.Button(master, font=("Arial"), image=self.img, compound="top", command=atualiza_ponto_btn1)
        trunk_one.grid(row=7, column=0, padx=40, sticky="NESW")

        trunk_two = tk.Button(master, font=("Arial"), image=self.img, compound="top", command=atualiza_ponto_btn2)
        trunk_two.grid(row=7, column=1, padx=30, sticky="NESW")

        trunk_three = tk.Button(master, font=("Arial"), image=self.img, compound="top", command=atualiza_ponto_btn3)
        trunk_three.grid(row=7, column=2, padx=30, sticky="NESW")

        # Definir o mesmo tamanho para todas as colunas
        for i in range(3):
            master.columnconfigure(i, weight=1)


root = tk.Tk()
my_app = App(root)
root.mainloop()

