from abc import ABC, abstractmethod


class Figure(ABC):
    # dots of figure
    @abstractmethod
    def dots() -> list[(int, int)]:
        pass

    # RGB
    @abstractmethod
    def color() -> list[(int, int, int)]:
        pass

    @abstractmethod
    def command() -> str:
        pass
