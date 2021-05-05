from PPlay.window import *
from PPlay.sprite import *
from random import uniform
from random import randint
from PPlay.collision import *


def tiro_inimigo(janela,lista_nave_inimigas,time_tiro_enemy,lista,vel_tiro,nave,vida, i):
    
    if time_tiro_enemy >= 0.8:
        for A in lista_nave_inimigas:
            tiro  = Sprite(f"images/fase3/shot{i}A.png",5)
            print(i)
            tiro.set_position(A.x -140, A.y-42)
            tiro.set_total_duration(2000)
            lista.append(tiro)
            
        time_tiro_enemy = 0
    return lista, vida, time_tiro_enemy
