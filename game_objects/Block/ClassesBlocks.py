class Block:
    def __init__(self):
        super().__init__()
        self.size: list = [[]]
        self.shape: str = ""
        self.height: int = len(self.size)
        self.width: int = len(self.size[0])
        self.center: tuple[int, int]
        self.area: int = 0

    @staticmethod
    def rotate(degree: int) -> None:
        ...


class SquareBlock(Block):
    def __init__(self):
        super().__init__()
        self.size: list = [[]]
        self.shape: str = "square"
        self.height: int = len(self.size)
        self.width: int = len(self.size[0])


class SmallSquareBlock(SquareBlock):
    def __init__(self):
        super().__init__()
        self.size: list[list[int:]:] = [[1]]
        self.height: int = 1
        self.width: int = 1
        self.center = 0, 0
        self.area = 1


class MiddleSquareBlock(SquareBlock):
    def __init__(self):
        super().__init__()
        self.size: list[list[int]] = [[1, 1],
                                      [1, 1]]
        self.height: int = 2
        self.width: int = 2
        self.center = 0, 0
        self.area = 4


class BigSquareBlock(SquareBlock):
    def __init__(self):
        super().__init__()
        self.size: list[list[int]] = [[1, 1, 1],
                                      [1, 1, 1],
                                      [1, 1, 1]]
        self.height: int = 3
        self.width: int = 3
        self.center = 1, 1
        self.area = 9


class LBlock(Block):
    def __init__(self):
        super().__init__()
        self.size: list = [[]]
        self.shape: str = "L"
        self.height: int = len(self.size)
        self.width: int = len(self.size[0])


class SmallLBlock(LBlock):
    def __init__(self):
        super().__init__()
        self.size: list[list[int]] = [[1, 0],
                                      [1, 1]]
        self.default_size = self.size
        self.width = 2
        self.height = 2
        self.center = 0, 0
        self.area = 3

    def rotate(self, degree: int) -> None:
        match degree:
            case 90:
                self.size = [[1, 1],
                             [1, 0]]
            case 180:
                self.size = [[1, 1],
                             [0, 1]]
            case 270:
                self.size = [[0, 1],
                             [1, 1]]


class MiddleLBlock(LBlock):
    def __init__(self):
        super().__init__()
        self.size: list[list[int]] = [[1, 0],
                                      [1, 0],
                                      [1, 1]]
        self.default_size = self.size
        self.width = 2
        self.height = 3
        self.center = 1, 0
        self.area = 4

    def rotate(self, degree: int) -> None:
        match degree:
            case 90:
                self.size = [[1, 1],
                             [1, 0],
                             [1, 0]]
            case 180:
                self.size = [[1, 1],
                             [0, 1],
                             [0, 1]]
            case 270:
                self.size = [[0, 1],
                             [0, 1],
                             [1, 1]]


class BigLBlock(LBlock):
    def __init__(self):
        super().__init__()
        self.size: list[list[int]] = [[1, 0, 0],
                                      [1, 0, 0],
                                      [1, 1, 1]]
        self.default_size = self.size
        self.width = 3
        self.height = 3
        self.center = 1, 1
        self.area = 5


class PistolBlock(Block):
    def __init__(self):
        super().__init__()
        self.size: list = [[1, 0, 0],
                           [1, 1, 1]]
        self.default_size = self.size
        self.width: int = 3
        self.height: int = 2
        self.center = 1, 1
        self.area = 4

    def rotate(self, degree: int) -> None:
        self.size = self.default_size
        self.orientation_bias = degree
        match degree:
            case 90:
                self.size = [[1, 1, 1],
                             [1, 0, 0]]
            case 180:
                self.size = [[1, 1, 1],
                             [0, 0, 1]]
            case 270:
                self.size = [[0, 0, 1],
                             [1, 1, 1]]


class TBlock(Block):
    def __init__(self):
        super().__init__()
        self.size: list[list[int]] = [[1, 0],
                                      [1, 1],
                                      [1, 0]]
        self.default_size = self.size
        self.shape: str = "T"
        self.width = 2
        self.height = 3
        self.rotation: int = 0
        self.center = 1, 0
        self.area = 4

    def rotate(self, degree: int) -> None:
        match degree:
            case 90:
                self.size = [[1, 1, 1],
                             [0, 1, 0]]
            case 180:
                self.size = [[0, 1],
                             [1, 1],
                             [0, 1]]
            case 270:
                self.size = [[0, 1, 0],
                             [1, 1, 1]]


class IBlock(Block):
    def __init__(self):
        super().__init__()
        self.size: list = [[]]
        self.default_size = self.size
        self.height: int = len(self.size)
        self.width: int = len(self.size[0])


class SmallIBlock(IBlock):
    def __init__(self):
        super().__init__()
        self.size: list[list[int]] = [[1],
                                      [1]]
        self.default_size = self.size
        self.height = 2
        self.width = 1
        self.center = 0, 0
        self.area = 2

    def rotate(self, degree: int) -> None:
        if degree == 90 or degree == 270:
            self.size = [[1, 1]]


class MiddleIBlock(IBlock):
    def __init__(self):
        super().__init__()
        self.size: list[list[int]] = [[1],
                                      [1],
                                      [1]]
        self.default_size = self.size
        self.height = 3
        self.width = 1
        self.center = 1, 0
        self.area = 3

    def rotate(self, degree: int) -> None:
        if degree == 90 or degree == 270:
            self.size = [[1, 1, 1]]


class BigIBlock(IBlock):
    def __init__(self):
        super().__init__()
        self.size: list[list[int]] = [[1],
                                      [1],
                                      [1],
                                      [1]]
        self.default_size = self.size
        self.height = 4
        self.width = 1
        self.center = 1, 0
        self.area = 4

    def rotate(self, degree: int) -> None:
        if degree == 90 or degree == 270:
            self.size = [[1, 1, 1, 1]]


class HugeIBlock(Block):
    def __init__(self):
        super().__init__()
        self.size: list[list[int]] = [[1],
                                      [1],
                                      [1],
                                      [1],
                                      [1]]
        self.default_size = self.size
        self.height = 5
        self.width = 1
        self.center = 2, 0
        self.area = 5

    def rotate(self, degree: int) -> None:
        if degree == 90 or degree == 270:
            self.size = [[1, 1, 1, 1, 1]]


class LeftThunderBlock(Block):
    def __init__(self):
        super().__init__()
        self.size: list = [[0, 1],
                           [1, 1],
                           [1, 0]]
        self.default_size = self.size
        self.height = len(self.size)
        self.width = len(self.size[0])
        self.center = 0, 1
        self.area = 4

    def rotate(self, degree: int):
        if degree == 90 or degree == 270:
            self.size = [[1, 1, 0],
                         [0, 1, 1]]


class RightThunderBlock(Block):
    def __init__(self):
        super().__init__()
        self.size: list = [[1, 0],
                           [1, 1],
                           [0, 1]]
        self.default_size = self.size
        self.height = len(self.size)
        self.width = len(self.size[0])
        self.center = 0, 1
        self.area = 4

    def rotate(self, degree: int):
        if degree == 90 or degree == 270:
            self.size = [[0, 1, 1],
                         [1, 1, 0]]

