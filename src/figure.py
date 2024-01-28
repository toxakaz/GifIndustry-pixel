from abc import ABC, abstractmethod


class Figure(ABC):
    # dots of figure
    @abstractmethod
    def dots(self) -> list[(int, int)]:
        pass

    # RGB
    @abstractmethod
    def color(self) -> list[(int, int, int)]:
        pass

    @abstractmethod
    def command(self) -> str:
        pass

    # move the Figure
    @abstractmethod
    def shift(self, x_shift: int, y_shift: int) -> "Figure":
        pass