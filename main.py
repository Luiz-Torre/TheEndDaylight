from menu import menu_inicial
from tela_creditos import creditos
from tela_tutorial1 import tutorial1
from tela_tutorial2 import tutorial2 
from tela_tutorial3 import tutorial3
from game import fases
from tela_gameover import morreu


# Responsavel por fazer as trocas de tela
var_global = 0 

while True:
    if var_global == 0:
        var_global = menu_inicial()

    elif var_global == 1:
        var_global = fases(var_global)

    elif var_global == 2:
        var_global = morreu(var_global)

    elif var_global == 3:
        var_global = tutorial1()       

    elif var_global == 4:
        var_global = tutorial2() 
    
    elif var_global == 5:
        var_global = tutorial3() 

    elif var_global == 6:
        var_global = creditos()