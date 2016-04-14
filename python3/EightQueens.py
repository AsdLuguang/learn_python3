#!/usr/bin/python3

from tkinter import *

SIZE = 8
class EightQueens:
    def __init__(self):
        self.queens = SIZE * [-1]
        self.search(0)

        window = Tk()
        window.title("Eight Queens")

        for i in range(SIZE):
            for j in range(SIZE):
                if self.queens[i] == j:
                    Label(window, width = 5, height = 2,
                          bg = 'green').grid(row = i, column = j)
                else:
                    Label(window, width = 5, height = 2,
                          bg = 'red').grid(row = i, column = j)
        window.mainloop()

    def search(self, row):
        if row == SIZE:
            return True

        for column in range(SIZE):
            self.queens[row] = column
            if self.isValid(row, column) and self.search(row + 1):
                return True

        return False

    def isValid(self, row, column):
        for i in range(1, row + 1):
            if(self.queens[row - i] == column
               or self.queens[row - i] == column - i
               or self.queens[row - i] == column + i):
                return False
        return True

EightQueens()
