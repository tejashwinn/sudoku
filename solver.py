import random


def check_sub_box(puzzle, row, col, value):
    row = row-(row % 3)
    col = col-(col % 3)
    for i in range(3):
        for j in range(3):
            if puzzle[row+i][col+j] == value:
                return False


def check_valid(puzzle, value, row, col):  # sourcery skip: use-next
    for r in range(9):
        if puzzle[row][r] == value:
            return False
    for c in range(9):
        if puzzle[c][col] == value:
            return False
    return check_sub_box(row, col)


def search_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None


def sudoku_fill(puzzle):
    row, col = search_empty(puzzle)
    if row is None and col is None:
        return
    li = list(range(1, 10))
    for i in li:
        value = random.choice(li)
        li.remove(value)
        check_valid(puzzle, value, row, col)


puz = [[None for _ in range(9)] for _ in range(9)]
sudoku_fill(puz)
