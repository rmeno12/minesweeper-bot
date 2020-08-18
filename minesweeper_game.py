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

        # place mines and fill numbers
        # TODO: add i, j on bottom/right edges cases
        mines = random.sample(range(0, self.width * self.height), self.num_mines)
        mines = list(map(lambda x: (x // self.height, x % self.width), mines))
        for i in range(self.height):
            for j in range(self.width):
                # current spot should be a mine
                if (i, j) in mines:
                    out[i][j] = -1
                else:
                    to_check = []
                    if i == 0:
                        if j == 0:
                            to_check = [(0, 1), (1, 1), (1, 0)]
                        else:
                            to_check = [
                                (0, j - 1),
                                (1, j - 1),
                                (1, j),
                                (1, j + 1),
                                (0, j + 1),
                            ]
                    else:
                        if j == 0:
                            to_check = [
                                (i - 1, 0),
                                (i - 1, 1),
                                (i, 1),
                                (i + 1, 1),
                                (i + 1, 0),
                            ]
                        else:
                            to_check = [
                                (i - 1, j - 1),
                                (i, j - 1),
                                (i + 1, j - 1),
                                (i - 1, j),
                                (i + 1, j),
                                (i - 1, j + 1),
                                (i, j + 1),
                                (i + 1, j + 1),
                            ]
                    for thing in to_check:
                        if thing in mines:
                            out[i][j] += 1

        return out


game = MinesweeperGame(5, 5, 2)
