from collections import deque






empty = 0
start= 2
end = 3
wall = 1
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
            if n_row<0 or n_row>=grid.rows or n_col<0 or n_col>=grid.cols:
                print("block out of bounds")
                continue
            if neighbor in visited:
                print("block visited already twin")
                continue
            if grid.cells[n_row][n_col]==1:
                print("its a wall i cant go down there gang")
                continue
            print("shi is clean , proceeeding ")
            visited.add(neighbor)
            parent[neighbor]=current
            queue.append(neighbor)
            yield{
            'type':'added to frontier',
            'node':neighbor,
            'frontier':set(queue),
            'visited':visited.cop()}        
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
            'queue':set(stack),
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
                'queue':set(stack),
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
            if n_row<0 or n_row>=grid.rows or n_col<0 or n_col>=grid.cols:
                print("block out of bounds")
                continue
            if neighbor in visited:
                print("block visited already twin")
                continue
            if grid.cells[n_row][n_col]==1:
                print("its a wall i cant go down there gang")
                continue
            print("shi is clean , proceeeding ")
            visited.add(neighbor)
            parent[neighbor]=current
            stack.append(neighbor)  
            yield{
                'type':'added to frontier',
                'node':neighbor,
                'queue':set(stack),
                'visited':visited.copy()

            }       
    print("shi i m either too dumb or u did me dirty twin")
    return False
    




















if __name__=="__main__":
    mygrid=Grid(5,5)
    mygrid.set_cells(0, 0, start)    
    mygrid.set_cells(4, 4, end)     
    mygrid.set_cells(2, 2, wall)     
    mygrid.set_cells(2, 3, wall)
    mygrid.print_grid()
    print()
    bfs(mygrid,(0,0),(4,4))


