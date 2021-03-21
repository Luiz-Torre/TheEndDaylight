from PPlay.window import *
from PPlay.gameimage import *
#Inicialização

def morreu(var_global):
    janela = Window(1280,768)
    janela.set_title("The End Daylight")
    fundo_gameover = GameImage("gameover_imagens/fundo_perdeu.png")
    teclado = Window.get_keyboard()
    btn_tryagain = GameImage("gameover_imagens/button_tentenovamente.png")
    btn_tryagain.set_position(400,470)
    mouse = Window.get_mouse()
    while True:
        fundo_gameover.draw()
        btn_tryagain.draw()

        if mouse.is_over_object(btn_tryagain) and mouse.is_button_pressed(1): 
            var_global = 0
            return var_global


        janela.update()