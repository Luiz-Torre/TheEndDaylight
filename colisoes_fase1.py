from PPlay.collision import *

def tiro_asteroide(lista_tiro, lista_obstaculos):

    while True:
        
        if lista_tiro != [] and lista_obstaculos != []:
            for A in lista_obstaculos:
                for B in lista_tiro:
                    if B.y > A.y- A.height+30 and B.y < A.y+10 and B.x > A.x:
                        lista_obstaculos.pop(lista_obstaculos.index(A))

                        lista_tiro.pop(lista_tiro.index(B))



        return lista_tiro, lista_obstaculos