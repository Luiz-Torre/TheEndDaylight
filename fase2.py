from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import criando_mapa_fase2
from PPlay.collision import *
#Inicialização

#Corrigindo para a Amanda conseguir. PS: Python > C
def fase2(var_global):

    janela = Window(1280,768)
    janela.set_title("Fase 2 - The End Daylight")
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

    lista_chao = criando_mapa_fase2.criar(janela)
    cont =0
    fps = 0
    fps_atual = 0
    var = 1
    var2 = 1
    VelX= 100
    velY = 300
    jump1= False

    #Teste
    astronaut = []
    sprite_astrounaut = Sprite("images/fase2/run_1")
    sprite_astrounaut.set_position(0, 500)
    astronaut.append(sprite_astrounaut)

    sprite_astrounaut = Sprite("images/fase2/run_2")
    sprite_astrounaut.set_position(0, 500)
    astronaut.append(sprite_astrounaut)

    sprite_astrounaut = Sprite("images/fase2/run_3")
    sprite_astrounaut.set_position(0, 500)
    astronaut.append(sprite_astrounaut)

    sprite_astrounaut = Sprite("images/fase2/run_4")
    sprite_astrounaut.set_position(0, 500)
    astronaut.append(sprite_astrounaut)

    sprite_astrounaut = Sprite("images/fase2/run_5")
    sprite_astrounaut.set_position(0, 500)
    astronaut.append(sprite_astrounaut)

    sprite_astrounaut = Sprite("images/fase2/run_6")
    sprite_astrounaut.set_position(0, 500)
    astronaut.append(sprite_astrounaut)

    while True:

        #Teste
        velXmap = 120*janela.delta_time()         

        fundo.draw()
        pause_icon.draw()
        ## FrameRate
        cont += janela.delta_time()
        fps += 1
        if cont > 1:
            fps_atual = fps
            cont,fps = 0, 0


         ## Pausa
        if mouse.is_button_pressed(1) and mouse.is_over_object(pause_icon): 
            var = 0

        
        janela.draw_text(f"Fps: {fps_atual}", 800, 20, size=30, color=(240,240,240), font_name="Computer_says_no", italic=True)
        

        for move_personagem in astronaut:
            if(teclado.key_pressed("RIGHT")):
                fundo.move_x(-velXmap)
                move_personagem.move_x(VelX*janela.delta_time())
                move_personagem.update()

            if(teclado.key_pressed("LEFT") and move_personagem.x>0):
                fundo.move_x(velXmap)
                move_personagem.move_x(-VelX*janela.delta_time())
                move_personagem.update()
                
            if teclado.key_pressed("UP"):
                if(jump1):
                    velY = 250
                    move_personagem.move_y(-velY* janela.delta_time())
                jump1 = False

        for chao_draw in lista_chao:
            chao_draw.draw()
               
            for move_personagem in astronaut:
                if var2 == 1:
                    move_personagem.move_y(7)
                    var2=0

                if Collision.collided_perfect(chao_draw,move_personagem):
                    jump1 = True


            # if :

            
        if jump1 == False:
            for move_personagem in astronaut:

                move_personagem.move_y(-velY* janela.delta_time())  
                velY -= 200* janela.delta_time()


            

            
       
        move_personagem.draw()

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
                    var_global = 0
                    return var_global
