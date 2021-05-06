from PPlay.window import *
from PPlay.sprite import *
from random import uniform
from random import randint
from PPlay.collision import *
import unbounded_collision
from pygame import Rect


def tiro_inimigo(lista_nave_inimigas,time_tiro_enemy,lista,vel_tiro,nave,vida, i):
    
    if time_tiro_enemy >= 2:
        for A in lista_nave_inimigas:
            tiro  = Sprite(f"images/fase3/shot{i}A.png",5)
            tiro.set_position(A.x -140, A.y-42)
            tiro.set_total_duration(2000)
            lista.append(tiro)
        time_tiro_enemy = 0
    
    if lista:
        for B in lista:
            if B.x < 0:
                lista.pop(lista.index(B))

            if B.x <= nave.x and B.y+ B.height/2 > nave.y and B.y - B.height/2  < nave.y + nave.height and lista != []:
                lista.pop(lista.index(B))
                vida -= 1
            
    return lista, vida, time_tiro_enemy

def player_nave_inimigas(nave, lista_nave_inimigas,vida):

    while True:
        if  lista_nave_inimigas:
            for A in  lista_nave_inimigas:
                if Collision.collided_perfect(A,nave):
                        lista_nave_inimigas.pop( lista_nave_inimigas.index(A))
                        vida -= 1

        return  lista_nave_inimigas, vida