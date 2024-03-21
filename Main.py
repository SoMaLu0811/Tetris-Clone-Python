import pygame,sys
from Grid import Grid

#Tela do jogo

screen=pygame.display.set_mode((300, 600))
pygame.display.set_caption('Tetris')
clock=pygame.time.Clock()

game_grid=Grid()
game_grid.grid[0][0]=1
game_grid.grid[3][5]=4
game_grid.grid[17][8]=7

while True:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit()
            sys.exit
    #geração dos gráficos
    screen.fill(dark_blue)
    game_grid.draw(screen)
    pygame.display.update()
    clock.tick(60)
    
    
