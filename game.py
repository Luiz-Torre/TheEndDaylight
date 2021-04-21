from PPlay.window import *
from PPlay.gameimage import *
from fase1 import fase1
from fase2 import fase2
from fase3 import fase3

def transicao():
    janela = Window(1280,768)
    janela.set_title("Missao Concluida - The End Daylight")
    mouse = Window.get_mouse()

    fundo = GameImage("images/tela_geral/transition.png")
    aceitar = GameImage("images/tela_geral/accept.png")
    recusar = GameImage("images/tela_geral/refuse.png")

    aceitar.set_position(750, 608), recusar.set_position(350, 600)
    click = 0

    while True:
        fundo.draw()
        aceitar.draw()
        recusar.draw()
        
        click += janela.delta_time()

        if click > 1 and mouse.is_button_pressed(1): 
            if mouse.is_over_object(aceitar):
                return True
            if mouse.is_over_object(recusar):
                return False
        janela.update()

def fases(var):

    while True:
        if var == 1:
            var = fase1()
        elif var == 2:
            prox = transicao()
            if prox: var = fase2()
            else: var = 0
        elif var == 3:
            prox = transicao()
            if prox: var = fase3()
            else: var = 0
        # Morreu
        elif var == -1:
            return 2
        # Menu
        else:
            return 0


