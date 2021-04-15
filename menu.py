from PPlay.window import *
from PPlay.gameimage import *
#Inicialização


def menu_inicial():
    janela = Window(1280,768)
    janela.set_title("The End of Daylight")
    fundo_menu = GameImage("images/menu/fundo.png")

    btn_jogar = GameImage("images/menu/start.png")
    btn_comandos = GameImage("images/menu/comandos.png")
    btn_creditos = GameImage("images/menu/creditos.png")


    btn_jogar.set_position((janela.width)/2 - (btn_jogar.width)/2, janela.height -btn_comandos.height+55)
    btn_creditos.set_position(0, janela.height - btn_creditos.height+30)
    btn_comandos.set_position((janela.width)-btn_comandos.width, janela.height -btn_comandos.height+30)


    mouse = Window.get_mouse()
    click = 0

    #Game Loop
    while True:
        fundo_menu.draw()
        btn_jogar.draw()
        btn_creditos.draw()
        btn_comandos.draw()

        click += janela.delta_time()

        if click > 1 and mouse.is_button_pressed(1):
            click = 0
            if mouse.is_over_object(btn_jogar): 
                return 1

            if mouse.is_over_object(btn_creditos):
                return 6

            if mouse.is_over_object(btn_comandos):
                return 3   

        janela.update()
    
