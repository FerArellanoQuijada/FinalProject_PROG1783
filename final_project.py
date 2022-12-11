#Author: Fernando Arellano
#Creation Date: 2022/12/09 
#Modification Date: 2022/12/10
#Game: MineSweeper 
#Description: This game is a classic game called MineSweeper, the idea is to search places in the matrix in a safe place, if not a bomb will explode, if you choose a place safe you will be discovering  and sum points!


import random #Import module of random to put the bombs
import re #Import Module add patrons to identify strings 

class Board: #this load the new board
    def __init__(self, dimSize, numBombs):#Dimensions of the board
        self.dimSize = dimSize#define size
        self.numBombs = numBombs #define number of bomb

        self.board = self.makeNewBoard() # plant the bombs
        self.assignValues()

        self.dugged = set() #we need to enter 0,0 to put a position
        self.score = 0 #set variable score to cero 
    
    def welcome(self): #Welcome intro and explanation for the user, the idea is the same as classic minesweeper
        print("                ----------------------------------          ")
        print("                ***** Welcome to MineSweeper *****          ") #just a welcome message
        print("                 ----------------------------------          ")
        print("Minesweeper is single-player logic-based computer game played on rectangular board") #Little explain about how the game works. 
        print("whose object is to locate a predetermined number of randomly-placed 'mines' you need")
        print("to chosse by clicking on 'safe' places (squares) while avoiding the places without mines,")
        print("you will be earning point every time you clikc in a safe place.")
        print("            ----------------> Let's play! <----------------      ")



    def makeNewBoard(self): #This make the new board every time when the bomb is planted.  
        board = [[0 for _ in range (self.dimSize)] for _ in range(self.dimSize)]  #Create the 2D Board by console

        bombsPlanted = 0
        while bombsPlanted < self.numBombs:
            location = random.randint(0, self.dimSize**2 -1)
            row = location // self.dimSize #Indexes and position for rows
            column = location % self.dimSize #indexes and position for columns

            if board [row][column] == '*': #this is if plnted a bomb already so keep going 
                continue

            board[row][column] =  '*' #action to plant the  bomb
            bombsPlanted += 1

        return board

    def assignValues(self):# assign values to the loop an get the  neighbor spaces if there a bomb. 
        for r in range(self.dimSize):
            for c in range(self.dimSize):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.getNumNeighborBomb(r,c)

    def getNumNeighborBomb(self, row, column): #Function created to discover the places next to the selected area
        NumNeighborBomb = 0 
        for r in range(max(0, row-1),min(self.dimSize-1, row+1)+1): #to iterate each neighboard position and sum number of bombs
            for c in range (max(0, column-1), min(self.dimSize-1, column+1)+1):
                if r == row and c == column:
                    continue
                if self.board[r][c] == "*":
                    NumNeighborBomb +=1
        return NumNeighborBomb

    def dig(self, row, column): 
        self.dugged.add((row, column)) #keep the track of digginn

        if  self.board[row][column] == "*":
            return False
        elif self.board[row][column] > 0:
            self.score = len(self.dugged)
            return True
        for r in range(max(0, row-1), min(self.dimSize-1, row+1)+1):
            for c in range (max(0, column-1), min(self.dimSize-1, column+1)+1):
                if (r, c) in self.dugged:
                    continue #to not dig if is already digged by user
                self.dig(r, c)
        return True

    def __str__(self): #array to show what user sees
        visibleBoard = [[None for _ in range(self.dimSize)] for _ in range(self.dimSize)]
        for row in range(self.dimSize):
            for col in range(self.dimSize):
                if (row,col) in self.dugged:
                    visibleBoard[row][col] = str(self.board[row][col])
                else:
                    visibleBoard[row][col] = ' '

        widths = [] #Get max columns width fro printing
        for idx in range(self.dimSize):
            columns = map(lambda x: x[idx], visibleBoard)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        indices = [i for i in range(self.dimSize)]
        indicesRow = '    '
        for i in indices:
            if i < 10:
                indicesRow += f'{i}   '
            else:
                indicesRow += f'{i}  '
        indicesRow += '   \n'

        stringRep = ''
        for i in range(len(visibleBoard)):
            row = visibleBoard[i]
            if i < 10:
                stringRep += f'{i}  |'
            else:
                stringRep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = f'%-{str(widths[idx])}s'
                cells.append(format % (col))
            stringRep += '  |'.join(cells)
            stringRep += '  |\n'

        strLen = int(len(stringRep) / self.dimSize)
        stringRep = indicesRow + '-'*strLen + '\n' + stringRep + '-'*strLen

        return stringRep

#Play the game itself
def main(dimSize = 16, numBombs = 40):#The size of the board an the number of the bombs inside of it
    # sourcery skip: hoist-statement-from-if
    board = Board(dimSize, numBombs)
    board.welcome() #printing welcome
    while len(board.dugged) < board.dimSize ** 2 - numBombs:#if dug space get point and space between 
        print(board)
        print(f"Your current score is: {board.score}") #Prompt to show score every time. 
        userInput = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(userInput[0]), int(userInput[-1])
        if row < 0 or row >= board.dimSize or col < 0 or col >= dimSize:
            print("Invalid location. Try again.") #When you already show a place already taken
            continue

        safe = board.dig(row, col)#if user choose a place  not safe  break the while.
        if not safe:
            break

    if safe: #condition  to show if the user is in a safe place of not.
        print("Game Won!")
        print(f"Your final score was: {board.score}")#show the actul point
    else:
        print("Game Over!")#if not game over and show the final board.
        board.dugged = [(r,c) for r in range(board.dimSize) for c in range(board.dimSize)]
        print(board)
        print(f"Your final score was: {board.score}")
    

if __name__ == '__main__':
    main()