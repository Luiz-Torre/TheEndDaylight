from PPlay.window import *
from PPlay.gameimage import *
#Inicialização

def tutorial3():
    janela = Window(1280,768)
    janela.set_title("Tutorial Fase 3")

    fundo_gameover = GameImage("images/tela_tutorial/tutorial_fase3.png")

    btn_anterior = GameImage("images/tela_tutorial/anterior.png")
    btn_anterior.set_position(100,630)

    btn_voltar = GameImage("images/tela_tutorial/voltar_menu.png")
    btn_voltar.set_position(800,630)

    mouse = Window.get_mouse()
    click = 0
    
    while True:
        fundo_gameover.draw()
        btn_anterior.draw()
        btn_voltar.draw()

        click += janela.delta_time()

        if mouse.is_button_pressed(1) and click > 1:
            if mouse.is_over_object(btn_voltar): 
                return 0

            if mouse.is_over_object(btn_anterior): 
                return 4

        janela.update()