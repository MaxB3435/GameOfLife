from random import choice

GRID_W = 51
GRID_H = 51

#Size of cell == SZ

class Cell:
    def __init__(self,c,r,state=0):
        self.c = c
        self.r = r
        self.state = state
        
    def display(self):
        if self.state == 1:
            fill(0)
        else:
            fill(255)
        
        rect(SZ*self.r,SZ*self.c,SZ,SZ)
        
    def checkNeighbors(self):
        neighbs = 0 #check the neighbors
        
        for dr,dc in [[-1,-1],[-1,0],[-1,1],[1,0],[1,-1],[1,1],[0,-1],[0,1]]:
            try:
                if cellList[self.r + dr][self.c +dc].state == 1:
                    neighbs += 1
            except IndexError:
                continue
        if self.state == 1:
            if neighbs in [2,3]:
                return 1
            return 0
        if neighbs == 3:
            return 1
        return 0
    def checkMouse(self):

        if mouseY//SZ == self.c and mouseX//SZ == self.r: # if mouse on cell change state and keep all other cells the same
            if self.state == 0:
                return 1
            else: return 0
        elif self.state == 0:
            return 0
        elif self.state == 1:
            return 1
    
        
def setup():
    noStroke()
    global SZ,cellList
    size(600,600)
    SZ = width // GRID_W +1
    cellList = createCellList()

    
def draw():
  #  global cellList
    frameRate(30)
#    cellList = update(cellList)
#    for row in cellList:
#        for cell in row:
#            cell.display()

def keyPressed(): 
    global cellList
    cellList = update(cellList) # changes the cellList to the new list after an update
    for row in cellList:
        for cell in row:
            cell.display() # displays the new cells

    
    
    
        
def update(cellList):
    newList = [] # creats a new list
    for r,row in enumerate(cellList):
        newList.append([]) # adds empty row
        for c,cell in enumerate(row):
            newList[r].append(Cell(c,r,cell.checkNeighbors())) # adds a new cell in the row depending on the neighbors of the cell before the update
    return newList[::]    #returns the newList
    
            
def createCellList():
    newList=[] # creats an empty list
    for j in range(GRID_H): 
        newList.append([]) # adds empty row
        for i in range(GRID_W):
            newList [j].append(Cell(i,j,choice([0])))# adds off cells in the rows 
            

    return newList

def mousePressed():
    global cellList
    cellList = addCell(cellList) # changes current celllist to the celllist after adding a cell 
    for row in cellList:
        for cell in row:
            cell.display() # displays the new cellList


def addCell(cellList):
    newList = [] # creats a new list
    for r,row in enumerate(cellList):
        newList.append([]) # adds empty row
        for c,cell in enumerate(row):
            newList[r].append(Cell(c,r,cell.checkMouse())) # keeps cells the same except changes the state of the cell where the mouse is
    return newList[::]    #returns the newList 

            
             

        
    
    
