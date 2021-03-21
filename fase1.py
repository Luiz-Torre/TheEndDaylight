from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import nave_geral
#Inicialização

def fase(var_global):
    janela = Window(1280,768)
    fundo= GameImage("fase1_imagens/fundo.png") 
    janela.set_title("Fase 1 - The End Daylight")
    nave = Sprite("fase1_imagens/nave_sprite.png")
    nave.set_position(50,janela.height/2)
    teclado = Window.get_keyboard()
    lista_tiro = []
    temp = 0
    while True:
        fundo.draw()  
        nave.draw() 

        nave = nave_geral.movimentacao(janela,nave)

        vel_tiro = 600*janela.delta_time()
        temp+= janela.delta_time()

        lista_tiro,temp = nave_geral.tiro(janela,nave,lista_tiro,temp,vel_tiro)

        if(teclado.key_pressed("ESC")):
            var_global = 0
            return var_global

        janela.update()