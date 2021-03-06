from PPlay.window import *
from PPlay.sprite import *
from random import uniform
from random import randint
from PPlay.collision import *
import unbounded_collision
from pygame import Rect


def movimentacao(janela,nave_sprite):
    teclado = Window.get_keyboard()

    while True:
        vel_nave = 500*janela.delta_time()
        

        if(teclado.key_pressed("RIGHT")):
            if nave_sprite.x < janela.width - nave_sprite.width:
                nave_sprite.move_x(vel_nave)

        if(teclado.key_pressed("LEFT")):  
            if nave_sprite.x > 0 :
                    nave_sprite.move_x(-vel_nave)
        
        if(teclado.key_pressed("UP")):
            if nave_sprite.y > 0:
                nave_sprite.move_y(-vel_nave)

        if(teclado.key_pressed("DOWN")):  
            if nave_sprite.y < janela.height - nave_sprite.height :
                    nave_sprite.move_y(+vel_nave)

        return nave_sprite


def tiro(janela,nave_sprite,lista,temp,vel_tiro):
    teclado = Window.get_keyboard()

    while True:

        if teclado.key_pressed("SPACE") and temp > 0.4:

            tiro  = Sprite("images/fase1/shot.png",5)
            tiro.set_position(nave_sprite.x + 60, nave_sprite.y - 28)
            tiro.set_total_duration(1700)
            lista.append(tiro)
            temp = 0

        for A in lista:
                if A.x < janela.width:
                    A.move_x(vel_tiro)
                    A.update()
                    A.draw()
                else:
                    lista.pop(lista.index(A))
       
        return lista,temp

def inimigo(janela,lista_nave_inimigas,time,lista_tiro,pontos,time_tiro_enemy,lista,vel_tiro,nave,vida, i):
    if time >= 1.7:
        nave_inimiga_sprite = Sprite(f"images/fase3/Ship{i}.png", 1)
        nave_inimiga_sprite.set_position(1281+ randint(200,250),uniform(0,768- nave_inimiga_sprite.height-70))
        lista_nave_inimigas.append(nave_inimiga_sprite)
        time = 0


    for A in lista_nave_inimigas:
        if A.x >= 0- A.width:
            vel = 250*janela.delta_time()
            A.move_x(-vel)

            A.draw()
        else:
            lista_nave_inimigas.pop(lista_nave_inimigas.index(A))
        

        if lista_tiro:
            for B in lista_tiro:
                for A in lista_nave_inimigas:
                    if B.x >= A.x - A.width/2 and B.y+ B.height/2 > A.y and B.y - B.height/2  < A.y + A.height:
                        lista_nave_inimigas.pop(lista_nave_inimigas.index(A))
                        lista_tiro.pop(lista_tiro.index(B))
                        pontos += 1200 + 50*i

    return lista_nave_inimigas,time,lista_tiro,pontos, time_tiro_enemy,lista,vida

