from typing import Counter
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import criando_mapa_fase2
from PPlay.collision import *
#Inicialização

#Corrigindo para a Amanda conseguir. PS: Python > C KKKKKKKK tlgd
def fase2(pontos):

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

    ## Player
    vida, vida_list = 4, []
    for vida_num in range(1,vida):
            vida_img = Sprite("images/fase1/vida.png")
            vida_img.set_position(vida_num*50,20)
            vida_list.append(vida_img)

    lista_chao = criando_mapa_fase2.criar(janela)
    time = 0
    cont = 0
    fps = 0
    fps_atual = 0
    var = 1
    VelX= 90
    velY = 300
    jump = False

    #Teste
    astronaut = []
    for x in range (1,7):
        sprite_astrounaut = Sprite(f"images/fase2/run_{x}.png")
        sprite_astrounaut.set_position(10, 720 - sprite_astrounaut.height)
        astronaut.append(sprite_astrounaut)

    #var_anda = 0 --> sem uso
    count_chao = 0

    while True:

        ## Tela do Jogo
        fundo.draw()
        pause_icon.draw()
        janela.draw_text(f"Tempo 00:{60-time}", 450, 20, size=45, color=(240,240,240), font_name="Computer_says_no")
        janela.draw_text(f"Pontos {int(pontos)}", 650, 20, size=45, color=(240,240,240), font_name="Computer_says_no")
        janela.draw_text(f"Fps: {fps_atual}", 800, 20, size=30, color=(240,240,240), font_name="Computer_says_no", italic=True)
        
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
         
        ## Movimentacao
        if(teclado.key_pressed("RIGHT")):
            if astronaut[0].x >= janela.width/2:
                if fundo.x<= 0:
                    fundo.move_x(-velXmap)
                for a in lista_chao:
                    a.move_x(-VelX*janela.delta_time()- VelX*janela.delta_time() )

            else:        
                fundo.move_x(-velXmap)
                for a in lista_chao:
                    a.move_x(-VelX*janela.delta_time())
                astronaut[0].move_x(VelX*janela.delta_time())


        if teclado.key_pressed("LEFT"): #movimenta_personagem.x > 0 --> não existe
            astronaut[0].move_x(-VelX*janela.delta_time()*2)

        ## Pulo 
        # Obs: Mexi nele pois ao iniciar a fase o player estava morto, 
        # mas não acho que seja a melhor forma de implementar

        if teclado.key_pressed("UP"):
            if not jump:
                velY = 400
                astronaut[0].move_y(-velY * janela.delta_time())
            jump = True
        

        ## Plataforma
        for chao_draw in lista_chao:
            if chao_draw.x <= janela.width + 500:
                chao_draw.draw()
            if chao_draw.x <= 0 - chao_draw.width:
                lista_chao.pop(lista_chao.index(chao_draw))


        #for move_personagem in astronaut:
        for chao_draw in range(len(lista_chao)):

            if not Collision.collided_perfect(lista_chao[chao_draw],astronaut[0]):
                count_chao += 1
            else: 
                jump = False
                    
        if count_chao >= len(lista_chao):
            velY -= 100 * janela.delta_time()
            astronaut[0].move_y(-velY * janela.delta_time())  
            
        count_chao = 0


        ## Posição Astronaut
        # for i in astronaut:
        #     i.x = astronaut[0].x
        #     i.y = astronaut[0].y
        #     i.draw()
        astronaut[0].draw()
        if astronaut[0].y > janela.height:
            astronaut[0].y = 720 - sprite_astrounaut.height
            vida -= 1
        
        ## Gameover
        if vida == 0:
            return -1, pontos

        ## Proxima fase
        if time >= 60:
            return 2, pontos
        

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
                    return 0, pontos
