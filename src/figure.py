from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def dots() -> enumerate:
        pass
    @abstractmethod
    def color() -> enumerate:
        pass
    @abstractmethod
    def command() -> str:
        pass
