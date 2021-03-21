from PPlay.window import *
from PPlay.gameimage import *
#Inicialização

def tutorial(var_global):
    janela = Window(1280,768)
    janela.set_title("Tutorial Fase 1")
    fundo_gameover = GameImage("tela_tutorial_imagens/tutorial_fase2.png")
    btn_proximo = GameImage("tela_tutorial_imagens/proximo.png")
    btn_proximo.set_position(800,630)

    btn_anterior = GameImage("tela_tutorial_imagens/anterior.png")
    btn_anterior.set_position(100,630)
    mouse = Window.get_mouse()
    while True:
        fundo_gameover.draw()
        btn_proximo.draw()
        btn_anterior.draw()

        if mouse.is_over_object(btn_proximo) and mouse.is_button_pressed(1): 
            var_global = 5
            return var_global

        if mouse.is_over_object(btn_anterior) and mouse.is_button_pressed(1): 
            var_global = 3
            return var_global

        janela.update()