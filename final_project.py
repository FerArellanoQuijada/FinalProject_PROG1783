#Author: Fernando Arellano
#Creation Date: 2022/12/09 
#Modification Date
#Game: MineSweeper 
#Descrition:


import random
import re

class Board: 
    def __init__(self, dimSize, numBombs):
        self.dimSize = dimSize
        self.numBombs = numBombs

        self.board = self.makeNewBoard()
        self.assignValues()

        self.dugged = set()
        self.score = 0

    def makeNewBoard(self):
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

    def getNumNeighborBomb(self, row, column):
        NumNeighborBomb = 0 
        for r in range(max(0, row-1),min(self.dimSize-1, row+1)+1):
            for c in range (max(0, column-1), min(self.dimSize-1, column+1)+1):
                if r == row and c == column:
                    continue
                if self.board[r][c] == "*":
                    NumNeighborBomb +=1
        return NumNeighborBomb

    def dig(self, row, column):
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
        visible_board = [[None for _ in range(self.dimSize)] for _ in range(self.dimSize)]
        for row in range(self.dimSize):
            for col in range(self.dimSize):
                if (row,col) in self.dugged:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        string_rep = ''
        widths = []
        for idx in range(self.dimSize):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        indices = [i for i in range(self.dimSize)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dimSize)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep


def main(dimSize = 10, numBombs = 13):
    board = Board(dimSize, numBombs)
    while len(board.dugged) < board.dimSize ** 2 - numBombs:
        print(board)
        print(f"Your current score is: {board.score}")
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dimSize or col < 0 or col >= dimSize:
            print("Invalid location. Try again.")
            continue

        safe = board.dig(row, col)
        if not safe:
            break

    if safe:
        print("Game Won!")
        print(f"Your final score was: {board.score}")
    else:
        print("Game Over!")
        board.dugged = [(r,c) for r in range(board.dimSize) for c in range(board.dimSize)]
        print(board)
        print(f"Your final score was: {board.score}")
    

if __name__ == '__main__':
    main()