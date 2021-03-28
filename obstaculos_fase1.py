from PPlay.window import *
from PPlay.sprite import *
from random import randint


def asteroide(janela,time,lista_asteroide):
    
    if time > randint(1,3):

        asteroide = Sprite(f"images/fase1/asteroide{randint(1,3)}.png")
        asteroide.set_position(1281,randint(0 + asteroide.height,768- asteroide.height))
        lista_asteroide.append(asteroide)
        time = 0


    for obs in lista_asteroide:
        if obs.x > -100:
            vel = 320*janela.delta_time()
            obs.move_x(-vel)

            obs.draw()

        else:
            lista_asteroide.pop(lista_asteroide.index(obs))

    return lista_asteroide,time

def satelites_on(janela, time, lista_satelite_on,lista_tiros):

    if time > randint(2,4):
        satelite_on = Sprite("images/fase1/satellite_active.png")

        satelite_on.set_position(1281,randint(0 + satelite_on.height,768- satelite_on.height-randint(0,satelite_on.height+30)))

        lista_satelite_on.append(satelite_on)

        time = 0

    for obs in lista_satelite_on:
        if obs.x > -100:
            vel = 320*janela.delta_time()
            obs.move_x(-vel)

            obs.draw()

        else:
            lista_satelite_on.pop(lista_satelite_on.index(obs))


    return lista_satelite_on,time,lista_tiros

def satelites_off(janela, time, lista_obstaculos,lista_tiro):
        
        
        if time > randint(3,5):

            satelite_off = Sprite("images/fase1/satellite_dead.png")
            satelite_off.set_position(1281,randint(0 + satelite_off.height,768- satelite_off.height-80))
            lista_obstaculos.append(satelite_off)

            time = 0

    
        for obs in lista_obstaculos:
            if obs.x > -100:
                vel = 320*janela.delta_time()
                obs.move_x(-vel)

                obs.draw()

            else:
                lista_obstaculos.pop(lista_obstaculos.index(obs))

        return lista_obstaculos,time,lista_tiro



