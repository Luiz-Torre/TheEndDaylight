from PPlay.window import *
from PPlay.sprite import *


def criar(janela):
    lista_chao = []
    chao = Sprite("images/fase2/chao_azul_pequeno.png")
    chao.set_position(0,janela.height - chao.height+15)
    lista_chao.append(chao)
    i = 1
    while(i<70):
        if i%5 == 0:
            i = i +2
        

        if i%3 == 0:
            i = i+1

       
        chao = Sprite("images/fase2/chao_azul_pequeno.png")
        chao.set_position(108*i,janela.height - chao.height+15)
        lista_chao.append(chao)
        i += 1

        
    
 
    return lista_chao