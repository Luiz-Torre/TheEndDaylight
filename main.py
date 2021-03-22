import menu
import fase1
import tela_creditos
import fase2
import fase3
import tela_gameover
import tela_tutorial1
import tela_tutorial2
import tela_tutorial3


var_global = 0 #Responsavel por fazer as trocas de tela

while True:
    if var_global == 0:
        var_global = menu.menu_inicial(var_global)

    elif var_global == 1:
        var_global = fase1.fase(var_global)

    elif var_global == 2:
        var_global = tela_gameover.morreu(var_global)

    elif var_global == 3:
        var_global = tela_tutorial1.tutorial(var_global)       

    elif var_global == 4:
        var_global = tela_tutorial2.tutorial(var_global) 
    
    elif var_global == 5:
        var_global = tela_tutorial3.tutorial(var_global) 
 
