from PPlay.window import *
from PPlay.gameimage import *

def creditos():
    janela = Window(1280,768)
    janela.set_title("The End of Daylight - Creditos")

    fundo = GameImage("images/tela_creditos/credits.png")
    voltar = GameImage("images/tela_creditos/voltar_menu.png")
    voltar.set_position(1080, 650)

    mouse = Window.get_mouse()
    click = 0

    while True:
        fundo.draw()
        voltar.draw()

        click += janela.delta_time()

        if click > 0.5:
            if mouse.is_button_pressed(1) and mouse.is_over_object(voltar): 
                click = 0
                return 0

        janela.update()