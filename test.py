








#             DISCLAIMER : THIS SHI IS PURE HUMAN NOT A DAMN LINE IS FROM AI 









import pygame
import sys
from source2 import bfs,dfs,Button
ROWS=9
COLS=24
CELL_SIZE=40
WIDTH=COLS*CELL_SIZE
HEIGHT=ROWS*CELL_SIZE


WINDOW_HEIGHT=720
WINDOW_WIDTH=720
GIRID_OFFSET=360
WALL=1
START=2
END=3
EMPTY=0
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("fuckass pathfinder")
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)

WALLING=0
STARTING=1
ENDING=2
START_BFS=3
START_DFS=4
STATE_PATH=5

start_pos=None 
end_pos=None
stored=None
current_state=WALLING




search_running=0
search_engine=None
search_result=None
search_path=None



wall_button =Button(20,50,100,40,"WALLS",pygame.Color('gray'),pygame.Color('darkgray'))
start_button =Button(160,50,100,40,"START",pygame.Color('green'),pygame.Color('darkgreen'))
end_button =Button(300,50,100,40,"END",pygame.Color('red'),pygame.Color('darkred'))
clear_button =Button(420,50,100,40,"CLEAR",pygame.Color('blue'),pygame.Color('darkblue'))
bfs_button =Button(560,50,100,40,"BFS",pygame.Color('gold'),pygame.Color('darkgoldenrod'))
dfs_button =Button(20,100,100,40,"DFS",pygame.Color('lavender'),pygame.Color('plum'))






grid=[[0 for _ in range (COLS)] for _ in range (ROWS)]
def getcellmouse(pos):
     x,y=pos
     if y<GIRID_OFFSET:
         return None
     row=(y-GIRID_OFFSET)//40
     col=x//40
     print(f"nigga clicked on cell ({row},{col}) lmaooooo")
     return (row,col)
def drawgrid():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            y=GIRID_OFFSET+row*CELL_SIZE
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
            if search_running and search_result:
                current_cell= (row,col)
                if 'path'in search_result and current_cell in search_result['path']:
                    color = YELLOW
                elif search_result['type']=='exploring' and current_cell==search_result.get('node'):
                    color=BLUE
                elif current_cell in search_result.get('frontier',set()):
                    color=(0,100,255)
                elif current_cell in search_result.get('visited',set()):
                    color=(200,200,255)

            if not search_running and stored:
                if (row, col) in stored:
                    color = YELLOW








            pygame.draw.rect(screen,color,rect)
            pygame.draw.rect(screen,BLACK,rect ,1)







while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        wall_button.handle_event(event)
        start_button.handle_event(event)
        end_button.handle_event(event)
        clear_button.handle_event(event)
        bfs_button.handle_event(event)
        dfs_button.handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if wall_button.handle_event(event):
                current_state=WALLING
                print("adding walls currently*")
            elif start_button.handle_event(event):
                current_state=STARTING
                print("adding start bloc currently*")
            elif end_button.handle_event(event):
                current_state=ENDING
                print("adding end bloc currently*")
            elif clear_button.handle_event(event):
                grid=[[0 for _ in range (COLS)] for _ in range (ROWS)]
                search_running=False
                search_engine=None
                start_pos=None
                end_pos=None
                current_state=WALLING
                search_result=None
                print("grid cleared nigga")
            elif bfs_button.handle_event(event):
                if start_pos and end_pos:
                    print("starting bfs")
                    search_engine=bfs(grid,start_pos,end_pos)
                    search_running=True
                    current_state=START_BFS
                else:
                    print("set both start and end position negro ! ")
            elif dfs_button.handle_event(event):
                if start_pos and end_pos:
                    print("starting dfs")
                    search_engine=dfs(grid,start_pos,end_pos)
                    search_running=True
                    current_state=START_DFS 
            
            
            if getcellmouse(event.pos)==None:
                continue
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
    
                
                


    if search_running and search_engine:
        try:
            search_result=next(search_engine)

            if search_result['type']=='found':
                print("roger in that nigga")
                search_running=False
                search_engine=None
                search_path=search_result['path']
                stored=search_result['path']
        except StopIteration:
            print("fuh naw twin no results")
            search_running=False
            search_engine=None
    drawgrid() 
    wall_button.draw(screen)
    start_button.draw(screen)
    end_button.draw(screen)
    clear_button.draw(screen)
    bfs_button.draw(screen)
    dfs_button.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(5) 