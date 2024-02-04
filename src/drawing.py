import numpy as np
from PIL import Image, ImageDraw
from figure import Figure


def draw_figures(img: Image.Image | ImageDraw.ImageDraw, figures: list[Figure]) -> Image.Image:
    img_draw = ImageDraw.Draw(img) if type(img) is Image.Image else img
    for figure in figures:
        draw_figure(img_draw, figure)
    return img


def draw_figure(img: Image.Image | ImageDraw.ImageDraw, figure: Figure) -> Image.Image:
    img_draw = ImageDraw.Draw(img) if type(img) is Image.Image else img
    img_draw.polygon(figure.dots, figure.color, width=0)
    return img
