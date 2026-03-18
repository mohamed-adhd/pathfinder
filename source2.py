from collections import deque
import pygame




empty = 0
start= 2
end = 3
wall = 1

#             DISCLAIMER  / this button class is ai generated , ion got no time or mind for customizing damn python buttons , got bigger fish to fry twin


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=pygame.Color('white')):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False
        self.clicked = False
        
        # Load custom font (font.ttf in your folder)
        try:
            self.font = pygame.font.Font("font.ttf", 24)
        except:
            # Fallback to default font if custom font not found
            self.font = pygame.font.Font(None, 24)
            print("Custom font not found, using default")
    
    def handle_event(self, event):
        """Handle mouse events for the button"""
        if event.type == pygame.MOUSEMOTION:
            # Check if mouse is hovering
            self.is_hovered = self.rect.collidepoint(event.pos)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_hovered:  # Left click
                self.clicked = True
                return True
                
        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False
            
        return False
    
    def draw(self, screen):
        """Draw the button on screen"""
        # Choose color based on state
        if self.clicked:
            current_color = self.hover_color  # Darker when clicked
        elif self.is_hovered:
            current_color = self.hover_color  # Darker when hovered
        else:
            current_color = self.color
        
        # Draw button background with rounded corners
        pygame.draw.rect(screen, current_color, self.rect, border_radius=8)
        pygame.draw.rect(screen, pygame.Color('black'), self.rect, 2, border_radius=8)
        
        # Render text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        
        # Draw text
        screen.blit(text_surface, text_rect)
    
    def set_position(self, x, y):
        """Move button to new position"""
        self.rect.x = x
        self.rect.y = y
    
    def set_text(self, new_text):
        """Change button text"""
        self.text = new_text






class Grid:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.cells=[[0 for _ in range(cols)]for _ in range(rows)]
    def print_grid(self):
        symbols = {0: '⬜', 1: '⬛', 2: 'o🟢', 3: '⭕'}
        for row in self.cells :
            prows=[symbols[cell]for cell in row]
            print(' '.join(prows))
    def set_cells(self,row,col,type):
        if 0<=row<self.rows and 0<=col<=self.cols:
            self.cells[row][col]=type
    def get_cells(self,row,col):
        if 0<=row<=self.rows and 0<=col<=self.cols:
            return self.cells[row][col]



def bfs(grid,start,end):
    queue=deque([start])
    visited=set([start])
    parent={start:None}
    nodes_explored=0

    print(f"starting the bfs search for {end} from {start}")
    while queue:
        current=queue.popleft()
        nodes_explored+=1  
        yield{
            'type':'exploring',
            'node':current,
            'frontier':set(queue),
            'visited':visited.copy()}
        
        if current==end :
            path=[]
            step=current
            while step is not None:
                path.append(step)
                step=parent[step]
            path.reverse()
            yield{
            'type':'found',
            'node':current,
            'path':path,
            'visited':visited.copy()}
            print(f"target bamboozeled at {current},path : {path};\n")
            print("nodes explored :",nodes_explored)
            return True
        row,col=current
        neighbors=[(row-1,col),(row,col-1),(row+1,col),(row,col+1)]
        print("check for neighbors")
        for neighbor in neighbors :
            n_row,n_col=neighbor
            if n_row<0 or n_row>=len(grid) or n_col<0 or n_col>=len(grid[0]):
                print("block out of bounds")
                continue
            if neighbor in visited:
                print("block visited already twin")
                continue
            if grid[n_row][n_col]==1:
                print("its a wall i cant go down there gang")
                continue
            print("shi is clean , proceeeding ")
            visited.add(neighbor)
            parent[neighbor]=current
            queue.append(neighbor)
            yield{
            'type':'added',
            'node':neighbor,
            'frontier':set(queue),
            'visited':visited.copy()}        
    print("shi i m either too dumb or u did me dirty twin")
    return False



def dfs(grid,start,end):
    stack=([start])
    visited=set([start])
    parent={start:None}
    nodes_explored=0
    print(f"starting the dfs search for {end} from {start}")
    while stack:
        current=stack.pop()
        nodes_explored+=1  
        yield{
            'type':'exploring',
            'node':current,
            'frontier':set(stack),
            'visited':visited.copy()}

        
        if current==end :
            path=[]
            step=current
            while step is not None:
                path.append(step)
                step=parent[step]
            path.reverse()
            yield{
                'type':'found',
                'node':current,
                'frontier':set(stack),
                'path':path
            }
            print(f"target bamboozeled at {current},path {path} : ;\n")
            print("nodes explored :",nodes_explored)
            return True
        row,col=current
        neighbors=[(row-1,col),(row,col-1),(row+1,col),(row,col+1)]
        print("check for neighbors")
        for neighbor in neighbors :
            n_row,n_col=neighbor
            if n_row<0 or n_row>=len(grid) or n_col<0 or n_col>=len(grid[0]):
                print("block out of bounds")
                continue
            if neighbor in visited:
                print("block visited already twin")
                continue
            if grid[n_row][n_col]==1:
                print("its a wall i cant go down there gang")
                continue
            print("shi is clean , proceeeding ")
            visited.add(neighbor)
            parent[neighbor]=current
            stack.append(neighbor)  
            yield{
                'type':'added',
                'node':neighbor,
                'frontier':set(stack),
                'visited':visited.copy()

            }       
    print("shi i m either too dumb or u did me dirty twin")
    return False
    






















