import random

from game_objects.Board.board import Board
from pygame.sprite import Group
from .ClassSquare import *
from .ClassesBlocks import *
from game_objects.Board.funcs import *


def placeable(block: Block) -> bool:
    temporary_board_copy: list
    squares_counter: int
    go_further: bool = False
    for y in range(0, 8):
        for x in range(0, 8):
            squares_counter = 0
            temporary_board_copy = Board.copy()
            for block_y in range(0, block.height - 1):
                for block_x in range(0, block.width - 1):
                    if y + block_y <= 7 and x + block_x <= 7:
                        temporary_board_copy[y + block_y][x + block_x] += block.size[block_y][block_x]
                        if temporary_board_copy[y + block_y][x + block_x] > 1:
                            go_further = True
                            squares_counter = 0
                            temporary_board_copy = Board.copy()
                            break
                        squares_counter += 1
                if go_further:
                    go_further = False
                    break
            if squares_counter == block.width * block.height:
                return True
    return False


def get_board_empty_space() -> int:
    counter: int = 0
    for y in range(0, 8):
        counter += Board[y].count(0)
    return counter


def get_placeable_blocks_names():
    keys: tuple = tuple(block_types.keys())
    block: Block
    empty_space: int = get_board_empty_space()
    placeable_blocks_names: list = []
    block_on_board_fragment: list = []
    for name in keys:
        block = block_types[name]
        if block.area <= empty_space:
            for i in range(8, block.width, -1):
                for block_row in block.size:
                    for j in range(8, block.width, -1):
                        block_row.append(0)
                    block_on_board_fragment.append(block_row)
                if block_on_board_fragment in Board:
                    placeable_blocks_names.append(name)


def set_option_pos(real_y: int, real_x: int, block_y: int, block_x: int) -> tuple[int, int]:
    return real_y + round(19 * block_y), real_x + round(19 * block_x)


def set_dragged_pos(real_y: int, real_x: int, block_y: int, block_x: int) -> tuple[int, int]:
    return real_y + round(47.5 * block_y), real_x + round(47.5 * block_x)


def get_random_block_object() -> Block:
    block_choice: str = random.choice(list(block_types.keys()))
    match block_choice:
        case "SmallSquareBlock":
            return SmallSquareBlock()
        case "MiddleSquareBlock":
            return MiddleSquareBlock()
        case "BigSquareBlock":
            return BigSquareBlock()
        case "SmallLBlock":
            return SmallLBlock()
        case "MiddleLBlock":
            return MiddleLBlock()
        case "BigLBlock":
            return BigLBlock()
        case "PistolBlock":
            return PistolBlock()
        case "TBlock":
            return TBlock()
        case "SmallIBlock":
            return SmallIBlock()
        case "MiddleIBlock":
            return MiddleIBlock()
        case "BigIBlock":
            return BigIBlock()
        case "HugeIBlock":
            return HugeIBlock()
        case "LeftThunderBlock":
            return LeftThunderBlock()
        case "RightThunderBlock":
            return RightThunderBlock()


def create_random_option(x: int, y: int) -> tuple[Group, Group]:
    global first_block_color
    global second_block_color
    global third_block_color
    global option_num
    option_color: str = choice(Square_colours)
    if option_num == 3:
        option_num = 1
    else:
        option_num += 1
    match option_num:
        case 1:
            first_block_color = option_color
        case 2:
            second_block_color = option_color
        case 3:
            third_block_color = option_color
    block: Block = get_random_block_object()
    # placeable_block_provided: bool = False
    # while not placeable_block_provided:
    #     if placeable(block):
    #         placeable_block_provided = True
    #     block = get_random_block_object()
    block_representation: list = block.size
    option_group: Group = Group()
    dragged_block_group: Group = Group()
    first_square: bool = True
    leader_i: int = 0
    leader_j: int = 0
    follower_bias: tuple[int, int] = 0, 0
    for i in range(0, block.height):
        for j in range(0, block.width):
            if block_representation[i][j] == 1:
                current_y, current_x = set_option_pos(y, x, j, i)
                option_group.add(Square((current_x, current_y), "option", color=option_color))
                current_y, current_x = set_option_pos(y, x, j, i)
                if first_square:
                    dragged_block_group.add(Square((current_x, current_y), "dragged", role="leader",
                                                   bias=follower_bias, color=option_color))
                    leader_i = i
                    leader_j = j
                    first_square = False
                else:
                    follower_bias = round(47.5 * (i - leader_i)), round(47.5 * (j - leader_j))
                    dragged_block_group.add(Square((current_x, current_y), "dragged", role="follower",
                                                   bias=follower_bias, color=option_color))
    return option_group, dragged_block_group


def get_new_square(position: tuple[int, int], color: str) -> Square:
    return Square(position, "regular", color=color)


def get_board_pos(x: int, y: int) -> tuple[int, int]:
    return 14 + y * 47, 200 + x * 47


def get_real_pos(x: int, y: int) -> tuple[int, int]:
    return round((y - 200) / 47), round((x - 14) / 47)


def get_squares_on_position() -> None:
    global first_block_color
    global second_block_color
    global third_block_color
    global option_num
    for i in range(0, 8):
        for j in range(0, 8):
            if (i, j) in freshly_modified_spots:
                if Board[i][j] == 1:
                    new_square_pos: tuple[int, int] = get_board_pos(i, j)
                    match option_num:
                        case 1:
                            new_square_color = first_block_color
                        case 2:
                            new_square_color = second_block_color
                        case 3:
                            new_square_color = third_block_color
                    if beginning_setup:
                        new_square_color = random.choice(Square_colours)
                    NEW_SQUARE: Square = get_new_square(new_square_pos, new_square_color)
                    SquaresGroup.add(NEW_SQUARE)
                    SquaresList.append(NEW_SQUARE)
                else:
                    for square in SquaresList:
                        if get_real_pos(square.rect.left, square.rect.top) == (i, j):
                            SquaresGroup.remove(square)
                            SquaresList.remove(square)


def fill_board_representation_with_block_representation(block_position: list[tuple[int, int]:]) -> None:
    for i in range(0, len(block_position)):
        Board[block_position[i][0]][block_position[i][1]] = 1
        freshly_modified_spots.append((block_position[i][0], block_position[i][1]))


def get_correct_block_placement(block: list) -> list[tuple[int, int]:]:
    correct_squares_placements: list[tuple[int, int]:] = []
    for square in block:
        correct_squares_placements.append(get_real_pos(square.pos[0] + square.bias[0], square.pos[1] + square.bias[1]))
    return correct_squares_placements


def try_place_block(block: list) -> bool:
    block_position: list[tuple[int, int]:] = get_correct_block_placement(block)
    for i in range(0, len(block_position)):
        if not 0 <= block_position[i][0] <= 7 or not 0 <= block_position[i][1] <= 7 or Board[block_position[i][0]][block_position[i][1]] == 1:
            return False
    fill_board_representation_with_block_representation(block_position)
    get_squares_on_position()
    return True


SquaresGroup = pygame.sprite.Group()
SquaresList: list[pygame.sprite:] = []

block_types: dict = {"SmallSquareBlock": SmallSquareBlock(),
                     "MiddleSquareBlock": MiddleSquareBlock(),
                     "BigSquareBlock": BigSquareBlock(),
                     "SmallLBlock": SmallLBlock(),
                     "MiddleLBlock": MiddleLBlock(),
                     "BigLBlock": BigLBlock(),
                     "PistolBlock": PistolBlock(),
                     "TBlock": TBlock(),
                     "SmallIBlock": SmallIBlock(),
                     "MiddleIBlock": MiddleIBlock(),
                     "BigIBlock": BigIBlock(),
                     "HugeIBlock": HugeIBlock(),
                     "LeftThunderBlock": LeftThunderBlock(),
                     "RightThunderBlock": RightThunderBlock()}

block_names: tuple = tuple(block_types.keys())
beginning_setup: bool = True
first_block_color: str = choice(Square_colours)
second_block_color: str = choice(Square_colours)
third_block_color: str = choice(Square_colours)
option_num: int = 1
