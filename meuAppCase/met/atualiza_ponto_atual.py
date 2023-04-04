#from numbers_to_string import show_value


""" def atualiza_ponto_btn1(current_point, trunk_result):
    current_point = trunk_result
    show_value(lbl_name, value)"""

def atualiza_ponto_btn1(self):
    self.pontoAtual = self.resultado_bau1
    #show_value(lbl_name, value) 
    self.label_pontuacao_atual.config(text=str(self.pontoAtual))

def atualiza_ponto_btn2(self):
    self.pontoAtual = self.resultado_bau2
    self.label_pontuacao_atual.config(text=str(self.pontoAtual))

def atualiza_ponto_btn3(self):
    self.pontoAtual = self.resultado_bau3
    self.label_pontuacao_atual.config(text=str(self.pontoAtual))