import pygame


def hovers(obj: pygame.rect.Rect) -> bool:
    if obj.left < pygame.mouse.get_pos()[0] < obj.right and obj.top < pygame.mouse.get_pos()[1] < obj.bottom:
        return True


def zerofy_list(obj: list, *, height: int, width: int) -> None:
    for i in range(0, height):
        for j in range(0, width):
            obj[i][j] = 0


def get_filled_list(*, height: int, width: int, content: int) -> list:
    obj: list = []
    for i in range(0, height):
        obj.append([])
        for j in range(0, width):
            obj.append(content)
    return obj
