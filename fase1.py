from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import nave_geral
import obstaculos_fase1
import colisoes_fase1
#Inicialização

def fase(var_global):
    janela = Window(1280,768)
    fundo= Sprite("fase1_imagens/fundo.png")
    fundo.set_position(0,0)
    fundo2= Sprite("fase1_imagens/fundo.png")
    fundo2.set_position(1280,0)
    janela.set_title("Fase 1 - The End Daylight")
    nave = Sprite("fase1_imagens/nave_sprite.png")
    lista_obstaculos = []
    nave.set_position(50,janela.height/2)
    teclado = Window.get_keyboard()
    lista_tiro = []
    temp = 0
    temp_tiro = 0
    temp_asteroide = 0
    vida = 3
    while True:
      
        vel_fundo = 0.2


        if  fundo.x+fundo.width>=0:
            fundo.move_x(-vel_fundo)  


        else:
            fundo.set_position(1280,0)

        if  fundo2.x+fundo2.width>=0:
            fundo2.move_x(-vel_fundo)  


        else:
            fundo2.set_position(1280,0)


        fundo.draw()
        fundo2.draw()
       

        nave.draw() 



        nave = nave_geral.movimentacao(janela,nave)

        vel_tiro = 600*janela.delta_time()
        temp_tiro+= janela.delta_time()
        temp_asteroide += janela.delta_time()

        lista_tiro,temp_tiro = nave_geral.tiro(janela,nave,lista_tiro,temp_tiro,vel_tiro)

        lista_obstaculos,temp_asteroide = obstaculos_fase1.asteroide(janela,temp_asteroide,lista_obstaculos)


        lista_tiro, lista_obstaculos= colisoes_fase1.tiro_asteroide(lista_tiro, lista_obstaculos)

        lista_obstaculos,vida = colisoes_fase1.nave_asteroide(nave, lista_obstaculos,vida)
       
        if(teclado.key_pressed("ESC")):
            var_global = 0
            return var_global


        if vida == 0:
            var_global = 0
            return var_global

        janela.update()