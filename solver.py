def search_empty(puzzle):

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] ==-1:
                return r, c
    return None, None


def sudoku_fill(puzzle):
    empty_row, empty_column = search_empty(puzzle)
    if empty_row is None and empty_column is None:
        return
    

puz = [[None for _ in range(9)] for _ in range(9)]
sudoku_fill(puz)
