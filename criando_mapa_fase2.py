from PPlay.window import *
from PPlay.sprite import *


def criar(janela):
    lista_chao = []
    chao = Sprite("images/fase2/chao_azul_pequeno.png")
    chao.set_position(0,janela.height - chao.height+15)
    lista_chao.append(chao)
    i = 1

    while i < 74:
        if i % 5 == 0:
            i += 4
            
        elif i % 6 == 0:
            i += 3
        else:
            i += 1

        chao = Sprite("images/fase2/chao_azul_pequeno.png")
        chao.set_position(108*i,janela.height - chao.height+15)
        lista_chao.append(chao)
    
    return lista_chao