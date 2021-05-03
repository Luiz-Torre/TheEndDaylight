from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import nave_geral
from PPlay.sound import *
import colisaofase3
from fase2 import fase2
#Inicialização

def fase3(pontos,vida):

    janela = Window(1280,768)
    janela.set_title("Fase 3 - The End of Daylight")
    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()

    fundo = Sprite("images/fase3/fundo.png")
    fundo.set_position(0,0)

    fundo2= Sprite("images/fase3/fundo.png")
    fundo2.set_position(1280,0)

    pause_icon = Sprite("images/pause/pause_icon.png")
    pause_icon.set_position(1280-pause_icon.width-30,10)


    som2 = Sound("sounds/Back to the Future with composer Alan Silvestri conducting in Vienna!_160k.ogg")
    som2.set_volume(100)


    nave = Sprite("images/fase3/nave.png")

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
    lista_nave_inimigas = []
    lista_tiro = []
    vida_list = []
    var, vida, pontos = 1, 4, 0

    for vida_num in range(1,vida):
        vida_img = Sprite("images/fase1/vida.png")
        vida_img.set_position(vida_num*50,20)
        vida_list.append(vida_img)

    #variáveis
    temp_tiro, temp_inimigo_nave, time_tiro_enemy= 0, 0, 0
    time, vida = 0, 4

    lista = []
    pausa_som = True
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
        temp_inimigo_nave += janela.delta_time()
        time_tiro_enemy += janela.delta_time()


        ## Setando tiros na tela
        lista_tiro,temp_tiro = nave_geral.tiro(janela,nave,lista_tiro,temp_tiro,vel_tiro)

        lista_nave_inimigas,temp_tiro,lista_tiro,pontos, time_tiro_enemy,lista,vida= nave_geral.inimigo(janela,lista_nave_inimigas,temp_tiro,lista_tiro,pontos,time_tiro_enemy,lista,vel_tiro,nave,vida)

        lista, vida, time_tiro_enemy = colisaofase3.tiro_inimigo(janela,lista_nave_inimigas,time_tiro_enemy,lista,vel_tiro,nave,vida)

        for shot in lista:
            shot.update()
            shot.draw()
            if shot.x < janela.width:
                        shot.move_x(-vel_tiro)

            else:
                lista.pop(lista.index(shot))
            
            # if shot.y< nave.y + nave.height-40 and shot.y> nave.y and shot.x <nave.x + nave.width:
            #     vida -= 1
            #     lista.pop(lista.index(shot))

        ## Desenhando vida
        for vida_for in range(vida-1):
            vida_list[vida_for].draw()

        ## Voltando para o menu
        if teclado.key_pressed("ESC"):
            return 0, pontos
        ## Gameover
        if vida == 0:
            return -1, pontos

        ## Proxima fase
        if time >= 60:
            som2.pause()
            som2.stop()
            

            return 2, pontos
    
        som2.play()


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
                    return 0, pontos
                # if mouse.is_over_object(music_on_pause) and som.is_playing():
                #     som.pause()
                #     pausa_som = False
                # if mouse.is_over_object(music_on_pause) and not som.is_playing():
                #     som.unpause()
                #     som.play()

                #     pausa_som = True

            


    return 0