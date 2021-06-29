import numpy as np
import random

qtde_num = {
    "impar": 7,
    "par": 8
}

def gerar_numeros(qtde_combinacoes):
    combinacoes = []
    jogo = []
    for combinacao in range(qtde_combinacoes):
        for numero_par in range(qtde_num.par):
             numero = random.randint(1,25,2)
             jogo.append(numero)
        for numero_impar in range(qtde_num.impar):
            numero = random.randint(1,26)
            
