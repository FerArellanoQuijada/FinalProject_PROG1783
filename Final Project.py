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
        
        self.dugged + set() #if we dig at 0,0, then self.dug + {(0,0)}

    def makeNewBoard(self): #this will be construct a new board based on the size and number of bombs

#Start thge game
def play (dimSize = 10, NumBombs = 10):
    #Step 1: Create the board
    #Step 2: Plant the bombs 
    #Step 3: Show board to select
    #step 3a: Show the board repeated times until the user find bombs 
    #Step 3b: If the user find a bomb, show game over message
    #step 4: Repeat steps until there is no more spaces or places to look up. 