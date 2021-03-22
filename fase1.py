from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import nave_geral
import obstaculos_fase1
import colisoes_fase1
#Inicialização

def fase(var_global):
    janela = Window(1280,768)
    fundo= GameImage("fase1_imagens/fundo.png") 
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
        fundo.draw()  
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