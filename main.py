import random

import pygame

from engine import funcs as engine
from game_objects.Block import funcs as BlockFunctions
from game_objects.Board import funcs as BoardFunctions
from game_objects.Button import ClassButton as ClBu
import game_state

pygame.init()
pygame.display.set_caption("Klocki!")
clock: pygame.time.Clock = pygame.time.Clock()

screen_width: int = 400
screen_height: int = 750
screen = pygame.display.set_mode((screen_width, screen_height))
font: pygame.font.Font = pygame.font.Font(None, 60)

ClassicGameModeButton: ClBu.Button = ClBu.Button("game_objects/Button/graphics/classic_game_mode_button", ".png")
TodoLaterModeButton: ClBu.Button = ClBu.Button("game_objects/Button/graphics/todo_later_mode_button", ".png")
GameModeButtonsGroup: pygame.sprite.Group = pygame.sprite.Group()
GameModeButtonsGroup.add(ClassicGameModeButton, TodoLaterModeButton)
GameModeButtons_list: list = [ClassicGameModeButton, TodoLaterModeButton]

RestartRoundButton: ClBu.Button = ClBu.Button("game_objects/Button/graphics/restart_round_button", ".png")
SettingsButtonGroup: pygame.sprite.GroupSingle = pygame.sprite.GroupSingle()
SettingsButtonGroup.add(RestartRoundButton)

MENU_DISPLAY: pygame.surface.Surface = pygame.image.load("graphics/main_menu_display/png.png")
CLASSIC_GAME_MODE_DISPLAY: pygame.surface.Surface = pygame.image.load("graphics/classic_game_mode_display/png.png")

OPTION_POS_ONE: tuple[int, int] = 60, 653
OPTION_POS_TWO: tuple[int, int] = 180, 653
OPTION_POS_THREE: tuple[int, int] = 300, 653
option_one: pygame.sprite.Group = pygame.sprite.Group()
option_one_rect: pygame.rect.Rect = pygame.rect.Rect(OPTION_POS_ONE[0], OPTION_POS_ONE[1], 95, 95)
option_one_rect.center = OPTION_POS_ONE[0], OPTION_POS_ONE[1]
option_one_in_use: bool = False
option_one_used: bool = False
option_two: pygame.sprite.Group = pygame.sprite.Group()
option_two_rect: pygame.rect.Rect = pygame.rect.Rect(OPTION_POS_TWO[0], OPTION_POS_TWO[1], 95, 95)
option_two_rect.center = OPTION_POS_TWO[0], OPTION_POS_TWO[1]
option_two_in_use: bool = False
option_two_used: bool = False
option_three: pygame.sprite.Group = pygame.sprite.Group()
option_three_rect: pygame.rect.Rect = pygame.rect.Rect(OPTION_POS_THREE[0], OPTION_POS_THREE[1], 95, 95)
option_three_rect.center = OPTION_POS_THREE[0], OPTION_POS_THREE[1]
option_three_in_use: bool = False
option_three_used: bool = False
block_one: pygame.sprite.Group = pygame.sprite.Group()
block_one_list: list[pygame.sprite:] = block_one.sprites()
block_two: pygame.sprite.Group = pygame.sprite.Group()
block_two_list: list[pygame.sprite:] = block_two.sprites()
block_three: pygame.sprite.Group = pygame.sprite.Group()
block_three_list: list[pygame.sprite:] = block_three.sprites()

used_block_length: int = 0

score_render = font.render(str(game_state.score), True, "white")

BEST_SCORE: str

with open("info/score.txt") as file:
    BEST_SCORE = file.read()

best_score_font: pygame.font.Font = pygame.font.Font(None, 40)
best_score_render = best_score_font.render(BEST_SCORE, True, "white")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if game_state.score > int(BEST_SCORE):
                with open("info/score.txt", "r+") as file:
                    file.truncate()
                    file.write(str(game_state.score))
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not option_one_in_use and not option_two_in_use and not option_three_in_use:
                game_state.round_start = True
                BlockFunctions.beginning_setup = True
            if event.key == pygame.K_t:
                pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                match game_state.display_mode:
                    case "Start menu":
                        if engine.hovers(ClassicGameModeButton.rect):
                            game_state.display_mode = "Classic game mode"
                    case "Classic game mode":
                        if engine.hovers(RestartRoundButton.rect):
                            game_state.beginning_setup_active = True
                            game_state.round_start = True
                            BlockFunctions.beginning_setup = True
                            game_state.score = 0
                            game_state.multiplier = 1
                        if game_state.held_block == "none":
                            if engine.hovers(option_one_rect):
                                game_state.held_block = "option one"
                                for square in block_one_list:
                                    square.held = True
                                option_one_in_use = True
                            elif engine.hovers(option_two_rect):
                                game_state.held_block = "option two"
                                for square in block_two_list:
                                    square.held = True
                                option_two_in_use = True
                            elif engine.hovers(option_three_rect):
                                game_state.held_block = "option three"
                                for square in block_three_list:
                                    square.held = True
                                option_three_in_use = True
                        else:
                            match game_state.held_block:
                                case "option one":
                                    BlockFunctions.option_num = 1
                                    option_one_used = BlockFunctions.try_place_block(block_one_list)
                                    used_block_length = len(block_one_list)
                                    if option_one_used:
                                        for square in block_one_list:
                                            square.held = False
                                        option_one_rect.topleft = 901, 2208
                                        game_state.score += used_block_length
                                    option_one_in_use = False
                                case "option two":
                                    BlockFunctions.option_num = 2
                                    option_two_used = BlockFunctions.try_place_block(block_two_list)
                                    used_block_length = len(block_two_list)
                                    if option_two_used:
                                        for square in block_two_list:
                                            square.held = False
                                        option_two_rect.topleft = 901, 2208
                                        game_state.score += used_block_length
                                    option_two_in_use = False
                                case "option three":
                                    BlockFunctions.option_num = 3
                                    option_three_used = BlockFunctions.try_place_block(block_three_list)
                                    used_block_length = len(block_three_list)
                                    if option_three_used:
                                        for square in block_three_list:
                                            square.held = False
                                        option_three_rect.topleft = 901, 2208
                                        game_state.score += used_block_length
                                    option_three_in_use = False
                            game_state.held_block = "none"
                            BoardFunctions.freshly_modified_spots.clear()
                            BoardFunctions.update_state()
                            BlockFunctions.get_squares_on_position()

    if game_state.game_active:
        match game_state.display_mode:
            case "Start menu":
                screen.blit(MENU_DISPLAY, (0, 0))

                GameModeButtonsGroup.draw(screen)
                GameModeButtonsGroup.update()

                if engine.hovers(ClassicGameModeButton.rect):
                    ClassicGameModeButton.shadow()
                else:
                    ClassicGameModeButton.unshadow()

                if engine.hovers(TodoLaterModeButton.rect):
                    TodoLaterModeButton.shadow()
                else:
                    TodoLaterModeButton.unshadow()

            case "Classic game mode":

                if game_state.beginning_setup_active:
                    BoardFunctions.fill_randomly()
                    game_state.beginning_setup_active = False
                    BoardFunctions.update_state()
                    BlockFunctions.get_squares_on_position()

                if game_state.round_start or option_one_used and option_two_used and option_three_used:
                    if not game_state.round_had_strike:
                        game_state.multiplier = 1
                    else:
                        game_state.multiplier += 1
                    BlockFunctions.option_num = 0
                    option_one, block_one = BlockFunctions.create_random_option(
                        OPTION_POS_ONE[0], OPTION_POS_ONE[1])
                    option_two, block_two = BlockFunctions.create_random_option(
                        OPTION_POS_TWO[0], OPTION_POS_TWO[1])
                    option_three, block_three = BlockFunctions.create_random_option(
                        OPTION_POS_THREE[0], OPTION_POS_THREE[1])
                    option_one_rect.center = OPTION_POS_ONE[0], OPTION_POS_ONE[1]
                    option_two_rect.center = OPTION_POS_TWO[0], OPTION_POS_TWO[1]
                    option_three_rect.center = OPTION_POS_THREE[0], OPTION_POS_THREE[1]
                    game_state.round_had_strike = False
                    game_state.round_start = False
                    BlockFunctions.beginning_setup = False
                    option_one_used = False
                    option_two_used = False
                    option_three_used = False
                    BoardFunctions.freshly_modified_spots.clear()

                block_one_list: list[pygame.sprite:] = block_one.sprites()
                block_two_list: list[pygame.sprite:] = block_two.sprites()
                block_three_list: list[pygame.sprite:] = block_three.sprites()

                screen.blit(CLASSIC_GAME_MODE_DISPLAY, (0, 0))

                SettingsButtonGroup.draw(screen)
                SettingsButtonGroup.update()

                if game_state.score > int(BEST_SCORE):
                    with open("info/score.txt", "r+") as file:
                        file.truncate()
                        file.write(str(game_state.score))
                    best_score_render = best_score_font.render(str(game_state.score), True, "white")

                score_render = font.render(str(game_state.score), True, "white")
                screen.blit(best_score_render, (85, 55))
                screen.blit(score_render, (200 - score_render.get_width() / 2, 150))

                if engine.hovers(RestartRoundButton.rect):
                    RestartRoundButton.shadow()
                else:
                    RestartRoundButton.unshadow()

                BlockFunctions.SquaresGroup.draw(screen)
                BlockFunctions.SquaresGroup.update()

                if not option_one_used and not option_one_in_use:
                    option_one.draw(screen)
                    option_one.update()

                if not option_two_used and not option_two_in_use:
                    option_two.draw(screen)
                    option_two.update()

                if not option_three_used and not option_three_in_use:
                    option_three.draw(screen)
                    option_three.update()

                match game_state.held_block:
                    case "option one":
                        block_one.draw(screen)
                        for square in block_one_list:
                            square.pos = pygame.mouse.get_pos()
                        block_one.update()
                    case "option two":
                        block_two.draw(screen)
                        for square in block_two_list:
                            square.pos = pygame.mouse.get_pos()
                        block_two.update()
                    case "option three":
                        block_three.draw(screen)
                        for square in block_three_list:
                            square.pos = pygame.mouse.get_pos()
                        block_three.update()

    pygame.display.flip()
    clock.tick(50)
