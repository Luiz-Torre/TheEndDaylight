from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import nave_geral
import obstaculos_fase1
import colisoes_fase1
#Inicialização


def fase(var_global):
    janela = Window(1280,768)
    janela.set_title("Fase 1 - The End Daylight")
    teclado = Window.get_keyboard()

    fundo= Sprite("images/fase1/fundo.png")
    fundo.set_position(0,0)

    fundo2= Sprite("images/fase1/fundo.png")
    fundo2.set_position(1280,0)

    nave = Sprite("images/fase1/ship.gif")
    fundo_pause = Sprite("images/pause/pause.png")
    continuar_pause = Sprite("images/pause/continuar.png")
    continuar_pause.set_position(500,300)

    pause_icon = Sprite("images/pause/pause_icon.png")
    pause_icon.set_position(1280-pause_icon.width-30,10)

    sair_pause = Sprite("images/pause/sair.png")
    sair_pause.set_position(500,400)

    mouse = Window.get_mouse()

    var = 1
    nave.set_position(50,janela.height/2)
    cont,fps = 0, 0
    fps_atual = 0
    lista_satelite_on = []
    lista_satelite_off = []
    lista_asteroide = []
    lista_tiro = []
    vida_list = []
    vida = 4
    pontos = 0
    for vida_num in range(1,vida):
        vida_img = Sprite("images/fase1/vida.png")
        vida_img.set_position(vida_num*50,20)
        vida_list.append(vida_img)

    #variáveis
    temp_tiro, temp_asteroide, temp_satelite_off,temp_satelite_on = 0, 0, 0, 0
    vida = 4

    while True:
        ####FrameRate
        cont += janela.delta_time()
        fps+=1
        if cont>1:
            fps_atual = fps
            cont=0
            fps=0


        vel_fundo = 0.2


        if  fundo.x+fundo.width>=0:
            fundo.move_x(-vel_fundo)  
        else:
            fundo.set_position(1280,0)

        
        if  fundo2.x+fundo2.width>=0:
            fundo2.move_x(-vel_fundo)  
        else:
            fundo2.set_position(1280,0)


        fundo.draw()
        fundo2.draw()
        pause_icon.draw()
        nave.draw() 



        nave = nave_geral.movimentacao(janela,nave)

        vel_tiro = 600*janela.delta_time()
        temp_tiro += janela.delta_time()
        temp_asteroide += janela.delta_time()
        temp_satelite_on += janela.delta_time()
        temp_satelite_off += janela.delta_time()


        if mouse.is_over_object(pause_icon) and mouse.is_button_pressed(1): 
                var = 0


        lista_tiro,temp_tiro = nave_geral.tiro(janela,nave,lista_tiro,temp_tiro,vel_tiro)

        lista_asteroide,temp_asteroide = obstaculos_fase1.asteroide(janela,temp_asteroide,lista_asteroide)
        lista_satelite_on,temp_satelite_on,lista_tiro = obstaculos_fase1.satelites_on(janela,temp_satelite_on,lista_satelite_on,lista_tiro)
        lista_satelite_off,temp_satelite_off,lista_tiro = obstaculos_fase1.satelites_off(janela,temp_satelite_off,lista_satelite_off,lista_tiro)


        lista_tiro, lista_asteroide= colisoes_fase1.tiro_obstaculo(lista_tiro, lista_asteroide)
        lista_satelite_on,lista_tiro,vida= colisoes_fase1.tiro_satelite_on(lista_tiro, lista_satelite_on,vida)
        lista_satelite_off,lista_tiro,pontos= colisoes_fase1.tiro_satelite_off(lista_tiro, lista_satelite_off,pontos)

        lista_asteroide, vida = colisoes_fase1.nave_asteroide(nave, lista_asteroide,vida)
       
        for vida_for in range(vida-1):
            vida_list[vida_for].draw()


        if(teclado.key_pressed("ESC")):
            var_global = 0
            return var_global


        if vida == 0:
            var_global = 0
            return var_global


        janela.draw_text(f"Pontos: {int(pontos)}", 400, 20, size=45, color=(240,240,240), font_name="Times New Roman", bold=True, italic=False)

        janela.draw_text(f"Fps: {fps_atual}", 800, 20, size=30, color=(240,240,240), font_name="Times New Roman", bold=True, italic=False)
        janela.update()

        while var == 0:
                
            fundo.draw()
            fundo2.draw()
            nave.draw()
            fundo_pause.draw()
            continuar_pause.draw()
            sair_pause.draw()
            janela.update()

            if mouse.is_over_object(continuar_pause) and mouse.is_button_pressed(1): 
                var = 1

            if mouse.is_over_object(sair_pause) and mouse.is_button_pressed(1):
                var_global = 0
                return var_global


            

