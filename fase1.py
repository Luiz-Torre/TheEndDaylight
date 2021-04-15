from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import nave_geral
import obstaculos_fase1
import colisoes_fase1
from fase2 import fase2
#Inicialização


def fase1():

    janela = Window(1280,768)
    janela.set_title("Fase 1 - The End Daylight")
    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()

    fundo = Sprite("images/fase1/fundo.png")
    fundo.set_position(0,0)

    fundo2= Sprite("images/fase1/fundo.png")
    fundo2.set_position(1280,0)

    pause_icon = Sprite("images/pause/pause_icon.png")
    pause_icon.set_position(1280-pause_icon.width-30,10)

    nave = Sprite("images/fase1/ship.gif")

    ## TELA DE PAUSA
    fundo_pause = Sprite("images/pause/pause.png")

    som_on_pause = Sprite("images/tela_geral/som_on.png")
    som_off_pause = Sprite("images/tela_geral/som_off.png")
    som_on_pause.set_position(500,330), som_off_pause.set_position(500,330)

    music_on_pause = Sprite("images/tela_geral/music_on.png")
    music_off_pause = Sprite("images/tela_geral/music_off.png")
    music_on_pause.set_position(680,330), music_off_pause.set_position(680,330)

    continuar_pause = Sprite("images/pause/continuar.png")
    continuar_pause.set_position(500,400)

    sair_pause = Sprite("images/pause/sair.png")
    sair_pause.set_position(500,500)


    ## Variáveis
    nave.set_position(50,janela.height/2)
    cont,fps, fps_atual = 0, 0, 0
    lista_satelite_on = []
    lista_satelite_off = []
    lista_asteroide = []
    lista_tiro = []
    vida_list = []
    var, vida, pontos = 1, 4, 0

    for vida_num in range(1,vida):
        vida_img = Sprite("images/fase1/vida.png")
        vida_img.set_position(vida_num*50,20)
        vida_list.append(vida_img)

    #variáveis
    temp_tiro, temp_asteroide, temp_satelite_off,temp_satelite_on = 0, 0, 0, 0
    time, vida = 0, 4

    while True:
        ## FrameRate
        cont += janela.delta_time()
        fps += 1
        if cont > 1:
            time += 1
            fps_atual = fps
            cont,fps = 0, 0

        ## Deslocamento de fundo
        vel_fundo = 0.2

        if  fundo.x+fundo.width>=0:
            fundo.move_x(-vel_fundo)  
        else:
            fundo.set_position(1280,0)

        if  fundo2.x+fundo2.width>=0:
            fundo2.move_x(-vel_fundo)  
        else:
            fundo2.set_position(1280,0)
        
        ## Desenhando tela do jogo
        fundo.draw()
        fundo2.draw()
        pause_icon.draw()
        janela.draw_text(f"Tempo 00:{60-time}", 450, 20, size=45, color=(240,240,240), font_name="Computer_says_no")
        janela.draw_text(f"Pontos {int(pontos)}", 650, 20, size=45, color=(240,240,240), font_name="Computer_says_no")
        janela.draw_text(f"Fps: {fps_atual}", 250, 20, size=30, color=(240,240,240), font_name="Computer_says_no", italic=True)
        nave.draw() 

        ## Pausa
        if mouse.is_button_pressed(1) and mouse.is_over_object(pause_icon): 
            var = 0

        ## Movimentação
        nave = nave_geral.movimentacao(janela,nave)

        ## Velocidade do tiro
        vel_tiro = 600*janela.delta_time()

        ## Variáveis de tempo
        temp_tiro += janela.delta_time()
        temp_asteroide += janela.delta_time()
        temp_satelite_on += janela.delta_time()
        temp_satelite_off += janela.delta_time()


        ## Setando tiros na tela
        lista_tiro,temp_tiro = nave_geral.tiro(janela,nave,lista_tiro,temp_tiro,vel_tiro)

        ## Setando obstáculos na tela
        lista_asteroide,temp_asteroide = obstaculos_fase1.asteroide(janela,temp_asteroide,lista_asteroide)
        lista_satelite_on,temp_satelite_on,lista_tiro = obstaculos_fase1.satelites_on(janela,temp_satelite_on,lista_satelite_on,lista_tiro)
        lista_satelite_off,temp_satelite_off,lista_tiro = obstaculos_fase1.satelites_off(janela,temp_satelite_off,lista_satelite_off,lista_tiro)

        ## Colisões por tiros
        lista_tiro, lista_asteroide = colisoes_fase1.tiro_obstaculo(lista_tiro, lista_asteroide)
        lista_satelite_on,lista_tiro,vida = colisoes_fase1.tiro_satelite_on(lista_tiro, lista_satelite_on,vida)
        lista_satelite_off,lista_tiro,pontos = colisoes_fase1.tiro_satelite_off(lista_tiro, lista_satelite_off,pontos)

        ## Colisões com obstáculos
        lista_asteroide, vida = colisoes_fase1.nave_asteroide(nave, lista_asteroide,vida)
        lista_satelite_on, vida = colisoes_fase1.nave_satelite_on(nave, lista_satelite_on,vida)
        lista_satelite_off, vida = colisoes_fase1.nave_satelite_off(nave, lista_satelite_off,vida)
       
        ## Desenhando vida
        for vida_for in range(vida-1):
            vida_list[vida_for].draw()

        ## Voltando para o menu
        if teclado.key_pressed("ESC"):
            exit()

        ## Gameover
        if vida == 0:
            return 2

        ## Proxima fase
        if time >= 60:
            return 2

        janela.update()

        ## TELA DE PAUSE
        while var == 0:
                
            fundo.draw()
            fundo2.draw()
            nave.draw()
            fundo_pause.draw()
            continuar_pause.draw()
            sair_pause.draw()
            music_on_pause.draw()
            som_on_pause.draw()

            janela.update()
            
            if mouse.is_button_pressed(1):
                if mouse.is_over_object(continuar_pause): 
                    var = 1

                if mouse.is_over_object(sair_pause):
                    return 0


            

