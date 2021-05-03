from PPlay.window import *
from PPlay.gameimage import *
from fase1 import fase1
from fase2 import fase2
from fase3 import fase3

def ini(janela, level):
    mouse = Window.get_mouse()
    click = 0

    fundo = GameImage(f"images/tela_geral/inifase{level}.png")
    jogar = GameImage("images/menu/start.png")
    jogar.set_position(1100, 600)

    while True:
        fundo.draw()
        jogar.draw()
        click += janela.delta_time()

        if click > 1 and mouse.is_button_pressed(1) and mouse.is_over_object(jogar):
            return True

        janela.update()


def transicao(level):
    janela = Window(1280,768)
    janela.set_title("Missao Concluida - The End of Daylight")
    mouse = Window.get_mouse()

    fundo = GameImage("images/tela_geral/transition.png")
    aceitar = GameImage("images/tela_geral/accept.png")
    recusar = GameImage("images/tela_geral/refuse.png")

    aceitar.set_position(750, 608), recusar.set_position(350, 600)
    click = 0

    if level == 1: 
        return ini(janela, level)

    while True:
        fundo.draw()
        aceitar.draw()
        recusar.draw()
        
        click += janela.delta_time()

        if click > 1 and mouse.is_button_pressed(1): 
            if mouse.is_over_object(aceitar):
                return ini(janela, level)
            if mouse.is_over_object(recusar):
                return False
        janela.update()

def fases(var,vida):
    
    while True:
        
        #Fase 1
        if var == 1:
            pontos = 0
            transicao(var)
            var, pontos = fase1()
            if var == 2:
                prox = transicao(var)
        
        # Fase 2
        elif var == 2:
            if prox: var, pontos, vida = fase2(pontos, vida)
            # Caso contrário volta para menu
            else: var = 0
        
        #Fase 3
        elif var == 3:
            prox = transicao(var)
            # Se aceitar continuar
            if prox: var = fase3(pontos, vida)
            # Caso contrário volta para menu
            else: var = 0
        
        # Morreu
        elif var == -1:
            return 2
        
        # Menu
        else:
            return 0


