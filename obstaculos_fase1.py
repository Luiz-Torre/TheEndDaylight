from PPlay.window import *
from PPlay.sprite import *
from random import randint


def asteroide(janela,time,lista_obstaculos):

    if time > randint(1,5):

        asteroide = Sprite("images/fase1/asteroide.png")
        asteroide.set_position(1281,randint(0 + asteroide.height,768- asteroide.height))
        lista_obstaculos.append(asteroide)

        time = 0


    for obs in lista_obstaculos:
        if obs.x > -100:
            vel = 200*janela.delta_time()
            obs.move_x(-vel)

            obs.draw()

        else:
            lista_obstaculos.pop(lista_obstaculos.index(obs))

    return lista_obstaculos,time

def satelites(janela, time, lista_obstaculos):

    if time > randint(2,5):
        satelite_on = Sprite("images/fase1/satellite_active.png")
        satelite_off = Sprite("images/fase1/satellite_dead.png")

        satelite_on.set_position(1281,randint(0 + satelite_on.height,768- satelite_on.height))
        satelite_off.set_position(1281,randint(0 + satelite_off.height,768- satelite_off.height))

        lista_obstaculos.append(satelite_on)
        lista_obstaculos.append(satelite_off)

        time = 0

    for obs in lista_obstaculos:
        if obs.x > -100:
            vel = 200*janela.delta_time()
            obs.move_x(-vel)

            obs.draw()

        else:
            lista_obstaculos.pop(lista_obstaculos.index(obs))

    return lista_obstaculos,time

