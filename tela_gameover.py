from PPlay.window import *
from PPlay.gameimage import *
#Inicialização


def morreu(var_global):
    janela = Window(1280,768)
    janela.set_title("The End Daylight")

    fundo_gameover = GameImage("images/gameover/fundo_perdeu.png")
    
    btn_tryagain = GameImage("images/gameover/button_tentenovamente.png")
    btn_tryagain.set_position(400,500)

    btn_return = GameImage("images/gameover/voltar_menu.png")
    btn_return.set_position(405,600)
    
    mouse = Window.get_mouse()

    while True:
        fundo_gameover.draw()
        btn_tryagain.draw()
        btn_return.draw()

        if mouse.is_button_pressed(1):
            if mouse.is_over_object(btn_return): 
                return 0
            if mouse.is_over_object(btn_tryagain): 
                return 1


        janela.update()