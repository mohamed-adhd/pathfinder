import pygame
import sys
ROWS=10
COLS=10
CELL_SIZE=50
WIDTH=COLS*CELL_SIZE
HEIGHT=ROWS*CELL_SIZE
WALL=1
START=2
END=3
EMPTY=0
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("fuckass pathfinder")
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)


WALLING=0
STARTING=1
ENDING=2
START_BFS=3
START_DFS=4
STATE_PATH=5

start_pos=None 
end_pos=None

current_state=WALLING
















grid=[[0 for _ in range (COLS)] for _ in range (ROWS)]
def getcellmouse(pos):
     x,y=pos
     row=y//50
     col=x//50
     print(f"nigga clicked on cell ({row},{col}) lmaooooo")
     return (row,col)
def drawgrid():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            y=row*CELL_SIZE
            x=col*CELL_SIZE
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
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_1:
                current_state=WALLING
                print("adding walls currently*")
            elif event.key == pygame.K_2:
                current_state=STARTING
                print("adding start bloc currently*")
            elif event.key==pygame.K_3:
                current_state=ENDING
                print("adding end bloc currently*")
            elif event.key==pygame.K_4:
                grid=[[0 for _ in range (ROWS)] for _ in range (COLS)]
                print("grid cleared nigga")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row,col=getcellmouse(event.pos)
            if (0<=row<ROWS and 0<=col<COLS):
                if current_state==WALLING:
                    if event.button==1:
                        grid[row][col]=1
                    elif event.button==3:
                        grid[row][col]=0
                if current_state==STARTING:
                    if (start_pos):
                        oldrow,oldcol=start_pos
                        grid[oldrow][oldcol]=0
                    grid[row][col]=2
                    start_pos=(row,col)
                if current_state==ENDING:
                    if (end_pos):
                        oldrow,oldcol=end_pos
                        grid[oldrow][oldcol]=0
                    grid[row][col]=3
                    end_pos=(row,col)
                
                


        drawgrid()
    pygame.display.flip()