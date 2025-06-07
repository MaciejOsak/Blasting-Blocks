from random import choice
import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], square_type: str = "regular", *, role: str = "none",
                 bias: tuple[int, int] = (0, 0), color: str = "pink"):
        super().__init__()
        self.type = square_type
        self.color = color
        match self.type:
            case "regular":
                self.image = pygame.image.load(f"game_objects/Block/graphics/square/{self.color}/png.png")
            case "option":
                self.image = pygame.image.load(f"game_objects/Block/graphics/option/{self.color}/png.png")
            case "dragged":
                self.image = pygame.image.load(f"game_objects/Block/graphics/square/{self.color}/png.png")
        self.role = role
        self.bias = bias
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.topleft = self.pos
        self.held = False

    def update(self):
        match self.type:
            case "regular":
                self.rect.topleft = self.pos
            case "option":
                self.rect.center = self.pos
            case "dragged":
                if self.held:
                    self.rect.topleft = self.pos[0] + self.bias[0], self.pos[1] + self.bias[1]
                else:
                    self.rect.topleft = self.pos[0], self.pos[1]


Square_colours: tuple[str:] = "blue", "green", "magenta", "navy", "orange", "pink", "red", "violet", "yellow"
SquaresGroup: pygame.sprite.Group = pygame.sprite.Group()
