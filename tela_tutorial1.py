from PPlay.window import *
from PPlay.gameimage import *
#Inicialização

def tutorial1():
    janela = Window(1280,768)
    janela.set_title("Tutorial Fase 1")

    fundo_gameover = GameImage("images/tela_tutorial/tutorial_fase1.png")

    btn_proximo = GameImage("images/tela_tutorial/proximo.png")
    btn_proximo.set_position(800,630)

    btn_voltar = GameImage("images/tela_tutorial/voltar_menu.png")
    btn_voltar.set_position(100,630)

    mouse = Window.get_mouse()
    click = 0

    while True:
        fundo_gameover.draw()
        btn_proximo.draw()
        btn_voltar.draw()

        click += janela.delta_time()

        if mouse.is_button_pressed(1) and click > 0.5:
            if mouse.is_over_object(btn_proximo): 
                return 4

            if mouse.is_over_object(btn_voltar): 
                return 0

        janela.update()