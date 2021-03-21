from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
#Inicialização

def fase(var_global):
    janela = Window(1280,768)
    fundo= GameImage("fase1_imagens/fundo.png") 
    janela.set_title("Fase 1 - The End Daylight")
    nave = Sprite("fase1_imagens/nave_sprite.png")
    nave.set_position(janela.width/2,janela.height/2)
    teclado = Window.get_keyboard()
    primeira = 0

    while True:
        fundo.draw()  
        nave.draw() 

        if(teclado.key_pressed("ESC")):
            var_global = 0
            return var_global



        janela.update()