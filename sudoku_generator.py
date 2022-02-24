import random


class SudokuGenerator:
    def __init__(self):
        self.generate_puzzle()
        self.li = list(range(1, 10))
        self.puzzle = [[self.li for _ in range(9)] for _ in range(9)]
        self.initial = random.randint(1, 9), random.randint(1, 9)

    # def generate_puzzle(self):
