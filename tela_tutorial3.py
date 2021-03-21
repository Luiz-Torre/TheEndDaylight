from PPlay.window import *
from PPlay.gameimage import *
#Inicialização

def tutorial(var_global):
    janela = Window(1280,768)
    janela.set_title("Tutorial Fase 1")
    fundo_gameover = GameImage("tela_tutorial_imagens/tutorial_fase3.png")
    btn_anterior = GameImage("tela_tutorial_imagens/anterior.png")
    btn_anterior.set_position(100,630)

    btn_voltar = GameImage("tela_tutorial_imagens/voltar_menu.png")
    btn_voltar.set_position(800,630)
    mouse = Window.get_mouse()
    while True:
        fundo_gameover.draw()
        btn_anterior.draw()
        btn_voltar.draw()

        if mouse.is_over_object(btn_voltar) and mouse.is_button_pressed(1): 
            var_global = 0
            return var_global

        if mouse.is_over_object(btn_anterior) and mouse.is_button_pressed(1): 
            var_global = 4
            return var_global

        janela.update()