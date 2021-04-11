from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import criando_mapa_fase2
from PPlay.collision import *
#Inicialização


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
    animacao  = Sprite("images/fase2/Astronaut_Run.png",6)
    animacao.set_position(0, 500)
    while True:

        #Teste
        velXmap = 120*janela.delta_time()

        animacao.set_total_duration(700)    
            


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
        


        if(teclado.key_pressed("RIGHT")):
            fundo.move_x(-velXmap)
            animacao.move_x(VelX*janela.delta_time())
            animacao.update()

        if(teclado.key_pressed("LEFT") and animacao.x>0):
            fundo.move_x(velXmap)
            animacao.move_x(-VelX*janela.delta_time())
            animacao.update()
            
        if teclado.key_pressed("UP"):
            if(jump1):
                velY = 300
                animacao.move_y(-velY* janela.delta_time())
            jump1 = False

        for chao_draw in lista_chao:
            chao_draw.draw()
               
            
            if var2 == 1:
                animacao.move_y(7)
                if Collision.collided_perfect(chao_draw,animacao):
                    var2=0

            if animacao.y >= chao_draw.y:
                jump1 = True 


        if jump1 == False:
            animacao.move_y(-velY* janela.delta_time())  
            velY -= 200* janela.delta_time()

       
        animacao.draw()

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
