import pygame,sys
from Grid import Grid
pygame.init()
dark_blue=(44,44,127)

#Tela do jogo

screen=pygame.display.set_mode((300, 600))
pygame.display.set_caption('Tetris')
clock=pygame.time.Clock()

game_grid=Grid()
game_grid.print_grid()

while True:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit()
            sys.exit
    #geração dos gráficos
    screen.fill(dark_blue )
    pygame.display.update()
    clock.tick(60)
    
    
