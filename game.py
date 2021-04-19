from fase1 import fase1
from fase2 import fase2
from fase3 import fase3

def fases(var):

    while True:
        if var == 2:
            var = fase1()
        elif var == 1:
            var = fase2()
        elif var == 3:
            var = fase3()
        # Morreu
        elif var == -1:
            return 2
        # Menu
        else:
            return 0