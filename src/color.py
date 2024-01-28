class Color:
    def __init__(self, r: int, g: int, b: int) -> None:
        self.color = (r, g, b)

    def __init__(self, color: (int, int, int)) -> None:
        self.color = color
