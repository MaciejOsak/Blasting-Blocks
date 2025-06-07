from random import randint
from .board import Board
import game_state


def fill_randomly() -> None:
    for i in range(0, 8):
        for j in range(0, 8):
            Board[i][j] = randint(0, 1)
            freshly_modified_spots.append((i, j))


def update_state():
    blocks_in_row: int
    horizontal_strikes: list = []
    vertical_strikes: list = []
    for i in range(0, 8):
        blocks_in_row = 0
        for j in range(0, 8):
            if Board[i][j] == 1:
                blocks_in_row += 1
            else:
                break
        if blocks_in_row == 8:
            horizontal_strikes.append(i)
    for i in range(0, 8):
        blocks_in_row = 0
        for j in range(0, 8):
            if Board[j][i] == 1:
                blocks_in_row += 1
            else:
                break
        if blocks_in_row == 8:
            vertical_strikes.append(i)
    for y in horizontal_strikes:
        for x in range(0, 8):
            Board[y][x] = 0
            freshly_modified_spots.append((y, x))
        game_state.score += 8 * game_state.multiplier * len(horizontal_strikes)
    for x in vertical_strikes:
        for y in range(0, 8):
            Board[y][x] = 0
            freshly_modified_spots.append((y, x))
        game_state.score += 8 * game_state.multiplier * len(vertical_strikes)
    if len(horizontal_strikes) != 0 or len(vertical_strikes) != 0:
        game_state.round_had_strike = True
        game_state.just_stroke = True


freshly_modified_spots: list[tuple:] = []
