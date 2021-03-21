from PPlay.window import *
#Inicialização

def fase(var_global):
    janela = Window(1280,768)
    janela.set_title("Fase 1 - The End Daylight")
    teclado = Window.get_keyboard()
    primeira = 0

    while True:
        janela.set_background_color((255,255,255))
        janela.draw_text(f"Demonstração fase 1. Pressione ESC para retornar", 50, 550, size=10, color=(0,0,0), font_name="Times New Roman", bold=True, italic=False)

        if(teclado.key_pressed("ESC")):
            var_global = 0
            return var_global



        janela.update()