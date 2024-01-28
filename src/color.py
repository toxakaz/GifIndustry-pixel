class Color:
    def __init__(self, r: int, g: int, b: int) -> None:
        self.rgb = (r, g, b)

    def __init__(self, color: (int, int, int)) -> None:
        self.rgb = color
