import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, path: str, extension: str):
        super().__init__()
        self.path: str = path
        self.image: pygame.surface.Surface = pygame.image.load(f"{path}/normal/png{extension}")
        self.rect: pygame.rect.Rect = self.image.get_rect()
        self.extension: str = extension

        match path:
            case "game_objects/Button/graphics/classic_game_mode_button":
                self.rect.topleft = (25, 520)
            case "game_objects/Button/graphics/todo_later_mode_button":
                self.rect.topleft = (85, 400)
            case "game_objects/Button/graphics/restart_round_button":
                self.rect.topleft = (330, 50)

    def shadow(self) -> None:
        self.image = pygame.image.load(f"{self.path}/shadowed/png{self.extension}")

    def unshadow(self) -> None:
        self.image = pygame.image.load(f"{self.path}/normal/png{self.extension}")

    def update(self):
        pass
