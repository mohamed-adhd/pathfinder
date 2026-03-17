import pygame
import sys
ROWS=10
COLS=10
CELL_SIZE=50
WIDTH=COLS*CELL_SIZE
HEIGHT=ROWS*CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("fuckass pathfinder")
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)


grid=[[0 for _ in range (COLS)] for _ in range (ROWS)]
def getcellmouse(pos):
     x,y=pos
     row=y//50
     col=x//50
     print(f"nigga clicked on cell ({row},{col}) lmaooooo")
def drawgrid():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            x=row*CELL_SIZE
            y=col*CELL_SIZE
            rect=pygame.Rect(x,y,CELL_SIZE,CELL_SIZE)
            if grid[row][col]==1 :
                color=BLACK
            elif grid[row][col]==3 :
                color=RED
            elif grid[row][col]==2 :
                color=GREEN
            else:
                color=WHITE
            pygame.draw.rect(screen,color,rect)
            pygame.draw.rect(screen,BLACK,rect ,1)







while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            getcellmouse(event.pos)
        drawgrid()
    pygame.display.flip()