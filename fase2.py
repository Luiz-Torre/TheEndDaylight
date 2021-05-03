from typing import Counter
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import criando_mapa_fase2
from PPlay.collision import *
from PPlay.sound import *
#Inicialização

#Corrigindo para a Amanda conseguir. PS: Python > C KKKKKKKK tlgd
def fase2(pontos,vida):

    janela = Window(1280,768)
    janela.set_title("Fase 2 - The End of Daylight")
    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()
    
    fundo = Sprite("images/fase2/fundo.png")
    pause_icon = Sprite("images/pause/pause_icon.png")
    pause_icon.set_position(1280-pause_icon.width-30,10)

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
    lista_det = []
    ## Player
    vida_list = []
    for vida_num in range(1,vida):
            vida_img = Sprite("images/fase1/vida.png")
            vida_img.set_position(vida_num*50,20)
            vida_list.append(vida_img)

    lista_chao, lista_acid, matriz_obs, lista_det, nave_fase2 = criando_mapa_fase2.criar(janela)
    time = 0
    cont = 0
    fps = 0
    fps_atual = 0
    var = 1
    VelX= 90
    velY = 300
    jump = True

    index = 0
    time_anda = 0
    som3 = Sound("sounds/Música de Suspense para Fundo de Vídeos 1 - Sem Direitos Autorais_160k.ogg")
    som3.set_volume(90)
    #Teste
    astronaut = [[],[]]
    for x in range (1,7):
        sprite_astrounaut = Sprite(f"images/fase2/run_{x}.png")
        sprite_astrounaut.set_position(10, 720 - sprite_astrounaut.height)
        astronaut[0].append(sprite_astrounaut)

    for x in range (1,7):
        sprite_astrounaut = Sprite(f"images/fase2/run_e{x}.png")
        sprite_astrounaut.set_position(10, 720 - sprite_astrounaut.height)
        astronaut[1].append(sprite_astrounaut)
        
    var_anda = 0
    count_chao = 0
    var_espinho = 0
    time_esp = 0
    evita_bug = 0
    while True:


            ## Tela do Jogo
            fundo.draw()
            pause_icon.draw()
            janela.draw_text(f"Tempo 00:{60-time}", 450, 20, size=45, color=(240,240,240), font_name="Computer_says_no")
            janela.draw_text(f"Pontos {int(pontos)}", 650, 20, size=45, color=(240,240,240), font_name="Computer_says_no")
            janela.draw_text(f"Fps: {fps_atual}", 800, 20, size=30, color=(240,240,240), font_name="Computer_says_no", italic=True)

            som3.play()

            for vida_for in range(vida-1):
                vida_list[vida_for].draw()

            ## Pausa
            if mouse.is_button_pressed(1) and mouse.is_over_object(pause_icon): 
                var = 0

            #Teste
            velXmap = 125*janela.delta_time()         

            ## FrameRate
            cont += janela.delta_time()
            fps += 1
            if cont > 1:
                time += 1
                fps_atual = fps
                cont,fps = 0, 0

            time_anda += janela.delta_time()
               
                    
 

            ## Movimentacao
            if(teclado.key_pressed("RIGHT") and evita_bug >=1):
                if astronaut[var_anda-1][index].x >= janela.width/2:
                    if fundo.x<= 0:
                        fundo.move_x(-velXmap)
                    for a in lista_chao:
                        a.move_x(-VelX*janela.delta_time()- VelX*janela.delta_time())
                    for a in lista_acid:
                        a.move_x(-VelX*janela.delta_time()- VelX*janela.delta_time())
                    for a in lista_det:
                        a.move_x(-VelX*janela.delta_time()- VelX*janela.delta_time())
                    for linha in matriz_obs:
                        for a in linha:
                            a.move_x(-VelX*janela.delta_time()- VelX*janela.delta_time())

                else:        
                    fundo.move_x(-velXmap)
                    for a in lista_chao:
                        a.move_x(-VelX*janela.delta_time())
                    for a in lista_acid:
                        a.move_x(-VelX*janela.delta_time())
                    for a in lista_det:
                        a.move_x(-VelX*janela.delta_time())
                    for linha in matriz_obs:
                        for a in linha:
                            a.move_x(-VelX*janela.delta_time())
                    astronaut[var_anda-1][index].move_x(VelX*janela.delta_time())
            
                var_anda = 1


            elif teclado.key_pressed("LEFT") and astronaut[var_anda-1][index].x > 0 and evita_bug >=1:
                astronaut[var_anda-1][index].move_x(-VelX*janela.delta_time()*2)
                var_anda = 2
            else:
                var_anda = 0

            if teclado.key_pressed("UP") and evita_bug >=1:
                var_anda = 1
                if jump:
                    velY = 215
                    astronaut[var_anda-1][index].move_y(-velY * janela.delta_time())
                    jump = False  
            


            

            if var_anda >= 1 and time_anda >= 0.1:

                index += 1
                time_anda = 0
                if index > 5: index = 0    

            elif var_anda == 0:
                index = 5
                var_anda = 1 


            astronaut[var_anda-1][index].draw()

            for linha in astronaut:
                for setando_posicao in linha:
                    setando_posicao.set_position(astronaut[var_anda-1][index].x,astronaut[var_anda-1][index].y)

            for acid_draw in lista_acid:
                if acid_draw.x <= janela.width + 50:
                    acid_draw.draw()

                if acid_draw.x <= 0 - acid_draw.width:
                    lista_acid.pop(lista_acid.index(acid_draw))
                    
                ## Perda de vida e fase é reiniciada
                if Collision.collided_perfect(astronaut[var_anda-1][index],acid_draw) and evita_bug >=1:
                    vida -= 1
                    return 2, pontos, vida

            
            ## Plataforma
            for chao_draw in lista_chao:
                if chao_draw.x <= janela.width + 50:
                    chao_draw.draw()
                if chao_draw.x <= 0 - chao_draw.width:
                    lista_chao.pop(lista_chao.index(chao_draw))

            
            # Movimentação do chão
            for chao_draw in range(len(lista_chao)):

                if not Collision.collided_perfect(lista_chao[chao_draw],astronaut[var_anda-1][index]) or astronaut[var_anda-1][index].y + 108> lista_chao[chao_draw].y+15:
                    count_chao += 1

                        
            if count_chao >= len(lista_chao):
                velY -= 150 * janela.delta_time()
                astronaut[var_anda-1][index].move_y(-velY * janela.delta_time())  
                jump = False
            else:
                jump = True

            count_chao = 0

            #Sprite de espinho
            if time_esp >= 0.5:
                var_espinho += 1
                time_esp = 0  

                if var_espinho > len(matriz_obs[0]) -1: var_espinho = 0
                


            for linha in matriz_obs:
                if linha[var_espinho].x <= janela.width + 50:
                    linha[var_espinho].draw()

                if linha[var_espinho].x <= 0 - linha[var_espinho].width:
                    matriz_obs.pop(matriz_obs.index(linha))
                    
                if Collision.collided_perfect(astronaut[var_anda-1][index],linha[var_espinho]) and evita_bug >=1 and var_espinho != 0:
                    vida -= 1
                    return 2, pontos, vida


            time_esp += janela.delta_time()

            for object in lista_det:

                if object.x <= janela.width + 50:
                    object.draw()

                if object.x <= 0 - object.width:
                    lista_det.pop(lista_det.index(object))
                    
                if Collision.collided_perfect(astronaut[var_anda-1][index],object) and evita_bug >=1:
                    pontos += 500
                    lista_det.pop(lista_det.index(object))


            ## Gameover
            if vida == -10 or time >= 300: # and not colided com nave no final
                som3.stop()

                return -1, pontos, vida

            ## Proxima fase
            # if colided com nave no final
            #     return 3, pontos, vida
            

            if evita_bug < 1:
                evita_bug += janela.delta_time()
            
            nave_fase2.draw()
            janela.update()

            ## TELA DE PAUSE
            while var == 0:
                    
                fundo.draw()
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
                        # som.stop()

                        return 0, pontos, vida
