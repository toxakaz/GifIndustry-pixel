from PIL import Image
from figure import Figure, Triangle
from utils import *


def triangulate_from_file(path: str) -> list[list[Figure]]:
    return triangulate(Image.open(path))


def triangulate(gif: Image.Image) -> list[list[Figure]]:
    raise NotImplementedError
