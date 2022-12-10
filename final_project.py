#Author: Fernando Arellano
#Creation Date: 2022/12/09 
#Modification Date
#Game: MineSweeper 
#Descrition:


import random
import re

class Board: #this load the new board
    def __init__(self, dimSize, numBombs):#Dimensions of the board
        self.dimSize = dimSize
        self.numBombs = numBombs

        self.board = self.makeNewBoard()
        self.assignValues()

        self.dugged = set()
        self.score = 0

    def makeNewBoard(self): #This make the new board every time when the bomb is planted.  
        board = [[0 for _ in range (self.dimSize)] for _ in range(self.dimSize)]

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
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.getNumNeighborBomb(r,c)

    def getNumNeighborBomb(self, row, column): #Function created to discover the places next to the selected area
        NumNeighborBomb = 0 
        for r in range(max(0, row-1),min(self.dimSize-1, row+1)+1):
            for c in range (max(0, column-1), min(self.dimSize-1, column+1)+1):
                if r == row and c == column:
                    continue
                if self.board[r][c] == "*":
                    NumNeighborBomb +=1
        return NumNeighborBomb

    def dig(self, row, column): #When the user dig a place will ad places next to the area. 
        self.dugged.add((row, column))

        if  self.board[row][column] == "*":
            return False
        elif self.board[row][column] > 0:
            self.score = len(self.dugged)
            return True
        for r in range(max(0, row-1), min(self.dimSize-1, row+1)+1):
            for c in range (max(0, column-1), min(self.dimSize-1, column+1)+1):
                if (r, c) in self.dugged:
                    continue
                self.dig(r, c)
        return True

    def __str__(self):
        visibleBoard = [[None for _ in range(self.dimSize)] for _ in range(self.dimSize)]
        for row in range(self.dimSize):
            for col in range(self.dimSize):
                if (row,col) in self.dugged:
                    visibleBoard[row][col] = str(self.board[row][col])
                else:
                    visibleBoard[row][col] = ' '
    
        widths = []
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
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            stringRep += '  |'.join(cells)
            stringRep += '  |\n'

        strLen = int(len(stringRep) / self.dimSize)
        stringRep = indicesRow + '-'*strLen + '\n' + stringRep + '-'*strLen

        return stringRep


def main(dimSize = 16, numBombs = 40):#The size of the board an the number of the bombs inside of it
    # sourcery skip: hoist-statement-from-if
    board = Board(dimSize, numBombs)
    while len(board.dugged) < board.dimSize ** 2 - numBombs:
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