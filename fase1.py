from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import nave_geral
import obstaculos_fase1
import colisoes_fase1
#Inicialização


def fase(var_global):
    janela = Window(1280,768)
    janela.set_title("Fase 1 - The End of Daylight")
    teclado = Window.get_keyboard()

    fundo= Sprite("images/fase1/fundo.png")
    fundo.set_position(0,0)

    fundo2= Sprite("images/fase1/fundo.png")
    fundo2.set_position(1280,0)

    nave = Sprite("images/fase1/ship.gif")
    nave.set_position(50,janela.height/2)
    
    pontos_text = GameImage("images/pontos.png")
    pontos_text.set_position(500,-5)
    #myfont = pygame.font.SysFont("Computer_says_no.ttf",25) 
    
    vida_list = []
    for vida_num in range(1,4):
        vida_img = Sprite("images/fase1/vida.png")
        vida_img.set_position(vida_num*50,20)
        vida_list.append(vida_img)

    #variáveis
    cont,fps, fps_atual, pontos = 0, 0, 0, 0
    lista_satelite_on, lista_satelite_off,lista_asteroide, lista_tiro = [], [], [], []
    temp_tiro, temp_asteroide, temp_satelite_off,temp_satelite_on = 0, 0, 0, 0
    vida = 3

    while True:
        #### FrameRate
        cont += janela.delta_time()
        fps += 1
        if cont > 1:
            fps_atual = fps
            cont, fps = 0, 0
        
        ### Fundo
        vel_fundo = 0.2
        if  fundo.x+fundo.width >= 0:
            fundo.move_x(-vel_fundo)  
        else:
            fundo.set_position(1280,0)

        if  fundo2.x+fundo2.width >= 0:
            fundo2.move_x(-vel_fundo)  
        else:
            fundo2.set_position(1280,0)


        fundo.draw()
        fundo2.draw()
       
        ### Nave
        nave.draw() 
        nave = nave_geral.movimentacao(janela,nave)

        ### Interações
        vel_tiro = 600*janela.delta_time()
        temp_tiro += janela.delta_time()
        temp_asteroide += janela.delta_time()
        temp_satelite_on += janela.delta_time()
        temp_satelite_off += janela.delta_time()


        lista_tiro,temp_tiro = nave_geral.tiro(janela,nave,lista_tiro,temp_tiro,vel_tiro)

        lista_asteroide,temp_asteroide = obstaculos_fase1.asteroide(janela,temp_asteroide,lista_asteroide)
        lista_satelite_on,temp_satelite_on,lista_tiro = obstaculos_fase1.satelites_on(janela,temp_satelite_on,lista_satelite_on,lista_tiro)
        lista_satelite_off,temp_satelite_off,lista_tiro = obstaculos_fase1.satelites_off(janela,temp_satelite_off,lista_satelite_off,lista_tiro)


        lista_tiro, lista_asteroide= colisoes_fase1.tiro_obstaculo(lista_tiro, lista_asteroide)
        lista_satelite_on,lista_tiro,vida= colisoes_fase1.tiro_satelite_on(lista_tiro, lista_satelite_on,vida)
        lista_satelite_off,lista_tiro,pontos= colisoes_fase1.tiro_satelite_off(lista_tiro, lista_satelite_off,pontos)

        lista_asteroide, vida = colisoes_fase1.nave_asteroide(nave, lista_asteroide,vida)
       
        for vida_for in range(vida):
            vida_list[vida_for].draw()


        if(teclado.key_pressed("ESC")):
            var_global = 0
            return var_global


        if vida == 0:
            var_global = 0
            return var_global

        pontos_text.draw()
        janela.draw_text(f"{int(pontos)}", 700, 20, size=40, color=(240,240,240), font_name="Times New Roman")
        janela.draw_text(f"Fps: {fps_atual}", 850, 20, size=30, color=(240,240,240), font_name="Times New Roman", italic=True)
        
        janela.update()