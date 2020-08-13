import random
from typing import List


class MinesweeperGame:
    def __init__(self, board_width: int, board_height: int, num_mines: int):
        super().__init__()
        self.width = board_width
        self.height = board_height
        self.num_mines = num_mines
        self.board = self.generate_board()

    def generate_board(self) -> List[List[int]]:
        # 1+ is nums, 0 is blank, -1 is mine, -2 is flag
        out = [[0] * self.width for _ in range(self.height)]

        # place mines
        mines = random.sample(range(0, self.width * self.height), self.num_mines)
        mines = list(map(lambda x: (x // self.height, x % self.width), mines))
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in mines:
                    out[i][j] = -1

        print(out)


game = MinesweeperGame(10, 10, 10)
