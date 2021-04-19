        if  not Collision.collided_perfect(chao_draw,move_personagem):
                    for move_personagem in astronaut:

                        move_personagem.move_y(-velY* janela.delta_time())  
                        velY -= 50* janela.delta_time()
