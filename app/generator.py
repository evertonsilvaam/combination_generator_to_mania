import numpy as np
import random
from random import sample

qtde_num = {
    "impar": 7,
    "par": 8
}

#gera lista com 15 números aleatórios de 1 a 25
def gerar_numeros(qtde_combinacoes):
    combinacoes = []
    
    for combinacao in range(qtde_combinacoes):
        
        for i in range(qtde_combinacoes):
            jogo = []
            sorteados = sample(range(1, 26), 15)
            sorteados.sort()
            jogo.append(sorteados)

        combinacoes.append(jogo)
    print(combinacoes)
            


gerar_numeros(5)