from PPlay.window import *
from PPlay.sprite import *


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

            

        if(teclado.key_pressed("SPACE") and temp > 0.5):

            tiro  = Sprite("images/fase1/shot.png",5)
            tiro.set_position(nave_sprite.x, nave_sprite.y-37)
            tiro.set_total_duration(2000)
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