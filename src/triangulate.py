from PIL import Image
from figure import Figure, Triangle


def triangulate_from_file(path: str) -> list[Figure]:
    return triangulate(Image.open(path))


def triangulate(gif: Image) -> list[Figure]:
    Triangle()
    return 0
