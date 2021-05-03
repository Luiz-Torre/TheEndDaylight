from random import uniform
from random import randint
from PPlay.window import *
from PPlay.sprite import *


def criar(janela):
    lista_chao = []
    lista_acid = []
    matriz_obs = []
    lista_obs = []
    matriz_det = []
    lista_det = []

    chao = Sprite("images/fase2/chao_azul_pequeno.png")
    chao.set_position(0,janela.height - chao.height+15)
    lista_chao.append(chao)
    i = 1
    r = 0

    acid = Sprite("images/fase2/small_acid.png")
    acid.set_position(108*i,janela.height - chao.height+25)
    lista_acid.append(acid)
    while i < 74:
        lista_obs = []

        if i % 5 == 0:
            valor = uniform(108*i+30,(108*(i+1)-50))
            for x in range (21,25):
                obs_espinho = Sprite(f"images/fase2/obs{x}.png")
                obs_espinho.set_position(valor, janela.height - chao.height -33)
                lista_obs.append(obs_espinho)
        
            matriz_obs.append(lista_obs)
            acid = Sprite("images/fase2/big_acid.png")
            acid.set_position(108*i,janela.height - chao.height+25)
            lista_acid.append(acid)
            r = i
            i += 4
            
        elif i % 4 == 0:
            valor = uniform(108*i+30,(108*(i+1)-50))
            for x in range (21,25):
                obs_espinho = Sprite(f"images/fase2/obs{x}.png")
                obs_espinho.set_position(valor, janela.height - chao.height -33)
                lista_obs.append(obs_espinho)
        
            matriz_obs.append(lista_obs)
            acid = Sprite("images/fase2/small_acid.png")
            acid.set_position(108*i,janela.height - chao.height+25)
            lista_acid.append(acid)
            r = i

            i += 3

        else:
            var_cria =randint(1,3)
            if var_cria == 2 and i!= 1:
                valor = uniform(108*i+30,(108*(i+1)-50))
                for x in range (21,25):
                    obs_espinho = Sprite(f"images/fase2/obs{x}.png")
                    obs_espinho.set_position(valor, janela.height - chao.height-33)
                    lista_obs.append(obs_espinho)
            
                matriz_obs.append(lista_obs)
#
            if var_cria == 3 or var_cria == 1 and i!= 1:
                valor = uniform(108*i+30,(108*(i+1)-50))
                det = Sprite(f"images/fase2/det2.png")
                det.set_position(valor, janela.height - chao.height-60)
                lista_det.append(det)
            
            r = i
            i += 1



        chao = Sprite("images/fase2/chao_azul_pequeno.png")
        chao.set_position(108*i,janela.height - chao.height+15)
        lista_chao.append(chao)

    nave_fase2 = Sprite("images/fase2/nave_2.png")
    nave_fase2.set_position(108*i,510)
        
    
    return lista_chao, lista_acid, matriz_obs, lista_det, nave_fase2