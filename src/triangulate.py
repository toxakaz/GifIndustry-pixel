from PIL import Image
from figure import Figure, Triangle
from utils import *


def triangulate_from_file(path: str) -> list[Picture]:
    return triangulate(Image.open(path))


def triangulate(gif: Image) -> list[Picture]:
    pass
