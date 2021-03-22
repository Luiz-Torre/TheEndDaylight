from PPlay.window import *
from PPlay.sprite import *
from random import randint
def asteroide(janela,time,lista_obstaculos):

    if time>randint(1,5):

        asteroide = Sprite("fase1_imagens/asteroide.png")
        asteroide.set_position(1281,randint(0 + asteroide.height,768- asteroide.height))
        lista_obstaculos.append(asteroide)
        time = 0


    for A in lista_obstaculos:
        if A.x > -100:
            vel = 200*janela.delta_time()
            A.move_x(-vel)

            A.draw()

        else:
            lista_obstaculos.pop(lista_obstaculos.index(A))

    return lista_obstaculos,time



    

