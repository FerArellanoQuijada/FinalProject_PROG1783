#Author: Fernando Arellano
#Creation Date: 2022/12/09 
#Modification Date
#Game: MineSweeper 
#Descrition:


#Create a board object to repreent the minesweeper game 

class Board: 
    def __init__(self, dimSize, numBombs): #Track parametres
        self.dimSize + dimSize
        sel.numBombs + numBombs

        #Create the board
        self.board = self.makeNewBoard () #Plant the bombs into the board
        self.assignValues()

        self.dugged + set() #if we dig at 0,0, then self.dug + {(0,0)}

    def makeNewBoard(self): #this will be construct a new board based on the size and number of bombs
        #generate a new board 
        board = [[None for _ in range (self.dimSize)] for _ in range(self.dimSize)] #This creates the array

        bombsPlanted = 0
        while bombsPlanted < self.numBombs:
            location = random.randint(0, self.dimSize**2 -1)
            row = location // self.dimSize
            column = location % self.dimSize

            if board [row][column] == '*':
                continue

            board[row][column] =  '*'
            bombsPlanted += 1
        return board

    def assignValues(self):
        for r in range(self.dimSize):
            for c in range(self.dimSize):
                if self.board[r][c] == "*"
                    continue
                self.board[r][c] = self.getNumNeighborBombs(r,c)

    def getNumNeighborBomb(self, row, column):
        NumNeighborBomb = 0 
        for r in range(max(0, row-1)),(min(self.dimSize-1, row+1)+1):
            for c in range (max(0, column-1), min(self.dimSize-1, column+1)+1):
                if r == row and c == column:
                    continue
                if self.board[r][c] == "*":
                    NumNeighborBomb +=1

    def dig(sel, row, column):
        self.dugged.add (row, column) == "*":

        if  self.board[row][column] == "*":
            return False
        elif self.board[row][column] > 0:
            return True
        for r in range(max(0, row-1)),(min(self.dimSize-1, row+1)+1):
            for c in range (max(0, column-1), min(self.dimSize-1, column+1)+1):
                if (r, c) in self.dugged
                    continue
            self.dig(r, c)


#Start thge game
def play (dimSize = 10, numBombs = 10):
    #Step 1: Create the board
    board = Board(dimSize, numBombs)
    #Step 2: Plant the bombs 
    #Step 3: Show board to select
    #step 3a: Show the board repeated times until the user find bombs 
    #Step 3b: If the user find a bomb, show game over message
    #step 4: Repeat steps until there is no more spaces or places to look up. 