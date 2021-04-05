from PPlay.collision import *

def tiro_obstaculo(lista_tiro, lista_obstaculos):

    if lista_tiro != [] and lista_obstaculos != []:
        for A in lista_obstaculos:
            for B in lista_tiro:
                if B.y > A.y- A.height and B.y < A.y and B.x >= A.x-A.width/2 and B.x<A.x:
                    lista_obstaculos.pop(lista_obstaculos.index(A))

                    lista_tiro.pop(lista_tiro.index(B))



    return lista_tiro, lista_obstaculos

def tiro_satelite_on(lista_tiros, lista_satelite_on,vida):
    if lista_tiros != [] and lista_satelite_on != []:
            for A in lista_satelite_on:
                for B in lista_tiros:
                    if B.y > A.y- A.height and B.y < A.y and B.x >= A.x-A.width/2 and B.x<A.x:
                        vida -= 1

                        lista_satelite_on.pop(lista_satelite_on.index(A))
                        lista_tiros.pop(lista_tiros.index(B))


    return lista_satelite_on,lista_tiros,vida


def tiro_satelite_off(lista_tiros, lista_satelite_off,pontos):
    if lista_tiros != [] and lista_satelite_off != []:
            for A in lista_satelite_off:
                for B in lista_tiros:
                    if B.y > A.y- A.height and B.y < A.y and B.x >= A.x-A.width/2 and B.x<A.x:
                        lista_satelite_off.pop(lista_satelite_off.index(A))
                        lista_tiros.pop(lista_tiros.index(B))
                        pontos += 1250
    return lista_satelite_off,lista_tiros,pontos

def nave_asteroide(nave, lista_asteroide,vida):

    while True:
        if lista_asteroide != []:
            for A in lista_asteroide:
                    if Collision.collided_perfect(A,nave):
                        lista_asteroide.pop(lista_asteroide.index(A))
                        vida -= 1

        return lista_asteroide, vida
